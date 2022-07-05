from django.shortcuts import render, HttpResponse
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
from django.db.models import Q
import csv



# Create your views here.
class CustomRegisterView(CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
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
        return context


class LogBookDataView(LoginRequiredMixin,ListView):
    model = LogBookData
    form_class = LogBookForm
    context_object_name = 'data'
    template_name = 'logbook/list_form.html' 

    def get_queryset(self):
        return LogBookData.objects.filter(user=self.request.user).order_by('-date_created')
    

   
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
    template_name = 'logbook/dashboard.html'



class ProfileFormView(LoginRequiredMixin,TemplateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'partials/profile.html'

class SearchListView(LoginRequiredMixin, ListView):
    model = LogBookData
    template_name = 'partials/logfilter.html'


def export_csv(request):
    response = HttpResponse(content_type ='text/csv')
    headers={'Content-Disposition': 'attachment; filename="logdata.csv"'}
    
    writer = csv.writer(response)
    writer.writerow(['patient fullname','patient gender','patient age',\
        'entry date','supervisor contact','hospital posted','biochemistry results','nutrition diagnosis','services rendered','clinical diagnosis','follow up plan','final outcome'])
    
    #query authenticated user data
    data = LogBookData.objects.filter(user=request.user)
    
    #loop through the user data 
    for d in data:
        writer.writerow(['d.patient fullname','d.patient gender','d.patient age','d.date','d.supervisor contact',\
            'd.hospital posted','d.biochemistry results','d.nutrition diagnosis','d.services rendered','d.clinical diagnosis',\
                'd.follow up plan','d.final outcome'])   


    return response


 
