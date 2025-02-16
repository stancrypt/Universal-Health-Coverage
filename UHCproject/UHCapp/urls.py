from . import views
from django.urls import path
from .views import get_name, submission_success, get_abi, submission_success1

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('charts/', views.charts, name='charts'),
    path('login/', views.get_name, name='login'),
    path('model/', views.model, name='model'),
    #path('submit/', get_name, name='submit_form'),
    #path('success/<int:form_id>/', submission_success, name='submission_success'), 
    path('phc/', views.get_abi, name='phc'),
    path('submit/', get_abi, name='submit_form'),
    path('success/<int:form_id>/', submission_success1, name='submission_success1'), 


   
]
