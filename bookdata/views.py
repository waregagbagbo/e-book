from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import LogBookForm,LogBookRegister,ProfileForm,LogBookSearchForm
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from django.core.paginator import Paginator

from django.db.models import Q
import csv


from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile




# Create your views here.
class CustomRegisterView(CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('user_login')
    form_class = LogBookRegister

        
       
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    fields = '__all__'
    redirect_authenticated_user = True    
# define a method to achieve the success url    
    def get_success_url(self):
        return reverse_lazy('dashboard')


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
        return content


class LogBookDataView(LoginRequiredMixin,ListView):
    model = LogBookData
    form_class = LogBookForm
    context_object_name = 'data'
    template_name = 'logbook/list_form.html' 
    paginate_by = 6 

    def get_queryset(self):
        return LogBookData.objects.filter(user=self.request.user).order_by('-date_created')

        search_input = self.request.GET.get('search_input') or ''
        if search_input:
            search = LogBookData.objects.filter(Q (patient_name__icontains=search_input))& Q(hospital__icontains=search_input)\
            & Q(patient_age__icontains=search_input)
        else:
            search = self.logBookData.objects.none()
        return search
    

   
class LogBookCreateView(LoginRequiredMixin,CreateView):
    model  = LogBookData
    form_class = LogBookForm
    template_name = 'logbook/create_form.html'
    success_url = 'main'

    def form_valid(self,form):
        form.instance.user = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class LogBookDelete(LoginRequiredMixin,DeleteView):
    model = LogBookData
    template_name = 'logbook/delete_form.html'
    success_url = reverse_lazy('main')

class DashboardView(TemplateView):
    template_name = 'logbook/index.html'


class ProfileFormView(LoginRequiredMixin,TemplateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'partials/profile.html'    

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
        'entry date','supervisor contact','hospital posted','biochemistry results','nutrition diagnosis','services rendered','clinical diagnosis','follow up plan','final outcome'])  
   
    
    #loop through the user data 
    for d in data:
        writer.writerow([d.patient_name, d.patient_gender,d.patient_age,d.date_created,d.supervisor_contact,\
            d.hospital,d.biochemistry_results,d.nutrition_diagnosis,d.services_rendered,d.clinical_diagnosis,\
                d.follow_up_plan,d.outcome]) 
    return response


#create pdf download

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



    

 
