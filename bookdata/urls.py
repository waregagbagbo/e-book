from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .views import LogBookDataView,LogBookCreateView,CustomRegisterView,\
    CustomLoginView,DashboardView,CustomLogoutView,\
        TemplateView,LogBookDelete,LogBookUpdate,ProfileFormView


urlpatterns = [
    path('', CustomLoginView.as_view(), name='user_login'),
    path('register',CustomRegisterView.as_view(),name='register'),
    path('logout',CustomLogoutView.as_view(), name='user_logout'),
    path('main',LogBookDataView.as_view(), name='main'),
    path('data', LogBookCreateView.as_view(), name='data'),
    path('dashboard',DashboardView.as_view(), name='dashboard'),
    path('profile/<int:pk>/', ProfileFormView.as_view(), name='profile'),
    path('delete_data/<int:pk>/',LogBookDelete.as_view(), name='delete_data'),
    path('update_details/<int:pk>/',LogBookUpdate.as_view(), name='update_details'),

    
    # document downloads path
    path('export', views.export_logbook, name='csv_file'),
    path('pdf_export', views.export_pdf, name='pdf'),


    # authentication section paths
    path('password_reset',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"),\
         name='reset_password'),

     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm_form.html"),\
         name='password_confirm'),

    path('password_done',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),\
         name='password_reset'),
    
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),\
         name='password_complete'),
         


   



    



]
