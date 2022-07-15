from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .views import LogBookDataView,LogBookCreateView,CustomRegisterView,\
    CustomLoginView,DashboardView,CustomLogoutView,ProfileFormView,TemplateView


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register',CustomRegisterView.as_view(),name='register'),
    path('logout',CustomLogoutView.as_view(), name='logout'),
    path('main',LogBookDataView.as_view(), name='main'),
    path('data', LogBookCreateView.as_view(), name='data'),
    path('dashboard',DashboardView.as_view(), name='dashboard'),
    path('profile', ProfileFormView.as_view(), name='profile'), 
    
    # document downloads path
    path('export_csv', views.export_logbook, name='csv_file'),
    path('export_pdf', views.export_pdf, name='pdf_file'),


    # authentication section paths
    path('password_reset',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"),\
         name='reset_password'),

     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_confirm_form.html"),\
         name='password_confirm'),

    path('password_change_form.html',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),\
         name='password_reset_done'),
    
    path('password_change_form.html',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),\
         name='password_reset_complete'),
         


   



    



]
