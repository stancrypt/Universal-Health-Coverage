from django.shortcuts import render
from django.http import HttpResponse
from . import chart

# Create your views here.

MDAs = ['CRSHIA', 'Service Providers','SACA']

def home(request):
    return render(request, 'uhc/home.html', )

def dashboard(request):
    return render(request, 'uhc/dashboard.html', )

def about(request):
    return render(request, 'uhc/about.html', )

def new_chart(request):
    charts=chart()
    return render(request, 'chart.html', {charts:chart})
