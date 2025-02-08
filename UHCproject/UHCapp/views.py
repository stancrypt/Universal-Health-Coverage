from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

MDAs = ['CRSHIA', 'Service Providers','SACA']

def home(request):
    return render(request, 'uhc/home.html', )

def dashboard(request):
    return render(request, 'uhc/dashboard.html', )

def index(request):
    return render(request, 'uhc/index.html', )
