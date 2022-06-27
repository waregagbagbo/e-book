from django.urls import path
from .import views
from .views import LogBookDataView,LogBookCreateView,CustomRegisterView,CustomLoginView,DashboardView,CustomLogoutView,ProfileFormView


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register',CustomRegisterView.as_view(),name='register'),
    path('logout',CustomLogoutView.as_view(), name='logout'),
    path('main',LogBookDataView.as_view(), name='main'),
    path('data', LogBookCreateView.as_view(), name='data'),
    path('dashboard',DashboardView.as_view(), name='dashboard'),
    path('profile', ProfileFormView.as_view(), name='profile'), 
]