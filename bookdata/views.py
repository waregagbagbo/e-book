from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import *
from .forms import LogBookForm,LogBookRegister,ProfileForm,UserUpdateForm
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,TemplateView,DetailView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.db.models import Q
import csv


from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile




# Create your views user registeration page section.
class CustomRegisterView(SuccessMessageMixin,CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('user_login')
    form_class = LogBookRegister
    success_message = "Account created successfully"

        
    # user login section   
class CustomLoginView(LoginView, SuccessMessageMixin):
    template_name = 'accounts/login.html'
    fields = '__all__'
    redirect_authenticated_user = True 
    success_message = "Login successfull" 

# define a method to achieve the success url    
    def get_success_url(self):
        return reverse_lazy('dashboard')


# user logout view section
class CustomLogoutView(LogoutView):
    template_name = 'accounts/logged_out.html'
    next_page = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
        'site': current_site,
        'site_name': current_site.name,
        'title': _('Logged out'),
        **(self.extra_context or {})
        })
        return context

# display total records
class LogBookDataView(LoginRequiredMixin,ListView):
    model = LogBookData
    form_class = LogBookForm
    context_object_name = 'data'
    template_name = 'logbook/list_form.html' 
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q') or '' 
        if q:
            multiple_q = Q(Q(patient_name__icontains=q) | Q(patient_age__icontains=q)) | Q(hospital__icontains=q)
            data =self.model.objects.filter(multiple_q)
        else:
            data = self.model.objects.none
        return LogBookData.objects.filter(user=self.request.user).order_by('-date_created')
        #return LogBookData.objects.filter(user=self.request.user).order_by('-date_created')
   
    
   # create an add operation form
class LogBookCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model  = LogBookData
    form_class = LogBookForm
    template_name = 'logbook/create_form.html'
    success_url = 'main'
    success_message = "Details saved successfully"    

    def form_valid(self,form):
        form.instance.user = self.request.user
        self.object = form.save()
        return super().form_valid(form)
   

# default dashboard view
class DashboardView(TemplateView):
    template_name = 'logbook/index.html'


# profile section view
class ProfileFormView(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'partials/profile.html'
    context_object_name = 'user'
    queryset = Profile.objects.all()
    #success_url = reverse_lazy('dashboard')

    def success_url(self):
        return reverse('users:user-settings', kwargs={'pk': self.get_object().id})

    def get_context_data(self, **kwargs):
        context = super(ProfileFormView, self).get_context_data(**kwargs)
        context['user'] = UserUpdateForm(instance=self.request.user)
        context["profile"] = ProfileForm(instance=self.request.user.profile)
        return context 

    def form_valid(self, form):
        profile = form.save(commit=False)
        user = profile.user
        user.last_name = form.cleaned_data['last_name']
        user.first_name = form.cleaned_data['first_name']
        user.save()
        profile.save()
        return HttpResponseRedirect(reverse('users:user-profile', kwargs={'pk': self.get_object().id}))

      
         

#delete view
class LogBookDelete(LoginRequiredMixin,DeleteView):
    model = LogBookData
    template_name = 'logbook/delete_form.html'
    success_url = reverse_lazy('main')

class LogBookUpdate(LoginRequiredMixin,UpdateView):
    model = LogBookData
    form_class = LogBookForm
    template_name = 'logbook/update_form.html'
    success_message = 'User data updated successfully'
    success_url = reverse_lazy('dashboard')  


# create csv download
def export_logbook(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'inline; attachment; filename=LogbookData.csv'

    #create the csv
    writer = csv.writer(response)

     #query authenticated user data
    data = LogBookData.objects.filter(user=request.user)
    # create row of items
    writer.writerow(['patientfullname','patient gender','patient age',\
        'entry date','supervisor contact','hospital posted','biochemistry results','nutrition diagnosis',\
            'services rendered','clinical diagnosis','follow up plan','final outcome'])  
   
    
    #loop through the user data 
    for d in data:
        writer.writerow([d.patient_name, d.patient_gender,d.patient_age,d.date_created,d.supervisor_contact,\
            d.hospital,d.biochemistry_results,d.nutrition_diagnosis,d.services_rendered,d.clinical_diagnosis,\
                d.follow_up_plan,d.outcome]) 
    return response


#create pdf download section
def export_pdf(request):
    response = HttpResponse(content_type ='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=LogbookData.pdf'

    response['Content-Transfer-Encoding'] = 'binary'

    data = LogBookData.objects.filter(user=request.user)

    html_string = render_to_string('partials/pdf.html',{'data':data})
    html = HTML(string = html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name,'rb')
        response.write(output.read())
    return response



    

 
