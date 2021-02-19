from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    # path('submitted', views.application_submitted, name='submitted'),home
    path('', views.home, name='home'),
    path('claim/category', views.select_category, name='select_category'),
    path('claim/motor_category/', views.motor_claim, name='motor_claim'),
    path('claim/life_category/', views.life_claim, name='life_claim'),
    # path('applications/<int:pk>/', views.delete_application, name='delete_application'),

    path('auth/register',views.register, name='register'),
    path('auth/login/',auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('auth/logout/',auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
]



