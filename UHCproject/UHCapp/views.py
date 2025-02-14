from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from .chart import calculate
from .login import NameForm

from .models import Person


# Create your views here.

MDAs = ['CRSHIA', 'Service Providers','SACA']

def home(request):
    return render(request, 'uhc/home.html', )

def dashboard(request):
    return render(request, 'uhc/dashboard.html', )

def about(request):
    return render(request, 'uhc/about.html', )

def model(request):
    person=Person()
    return render(request, 'uhc/models.html', {'person':person} )

def charts(request):
    cha= calculate()
    return render(request, 'uhc/chart.html', {'cha':cha})



def get_name(request):
    form = NameForm()
    return render(request, 'uhc/login.html', {'form': form})