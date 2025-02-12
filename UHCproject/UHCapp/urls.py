from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('chart/', views.charts, name='chart'),
    path('form/', views.get_name, name='form'),
    path('model/', views.model, name='model')

   
]
