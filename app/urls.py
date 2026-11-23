from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('recommend/', views.crop_recommendation_view, name='crop_recommendation'),
    path('history/', views.prediction_history_view, name='prediction_history'),
    path('crop-info/', views.crop_info_view, name='crop_info'),
    path('about-help/', views.about_help_view, name='about_help'),
]
