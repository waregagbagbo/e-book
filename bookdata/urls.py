from django.urls import path
from .import views
from .views import LogBookDataView,LogBookCreateView,CustomRegisterView,\
    CustomLoginView,DashboardView,CustomLogoutView,ProfileFormView,SearchListView


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register',CustomRegisterView.as_view(),name='register'),
    path('logout',CustomLogoutView.as_view(), name='logout'),
    path('main',LogBookDataView.as_view(), name='main'),
    path('data', LogBookCreateView.as_view(), name='data'),
    path('dashboard',DashboardView.as_view(), name='dashboard'),
    path('profile', ProfileFormView.as_view(), name='profile'), 
    path('search', SearchListView.as_view(), name='search'),

    path('export_csv', views.export_csv, name='csv_file'),



]