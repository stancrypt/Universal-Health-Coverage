from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from .chart import calculate
from .form import NameForm

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
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "uhc/form.html", {"form": form})