from django.shortcuts import render
from django.http import HttpResponse
from UHCapp.chart import calculate


# Create your views here.

MDAs = ['CRSHIA', 'Service Providers','SACA']

def home(request):
    return render(request, 'uhc/home.html', )

def dashboard(request):
    return render(request, 'uhc/dashboard.html', )

def about(request):
    return render(request, 'uhc/about.html', )

def charts(request):
    cha= calculate()
    return render(request, 'uhc/chart.html', {'cha':cha})
