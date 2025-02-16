from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .chart import calculate
from .login import NameForm, NameForm1
from .models import FormResponse, FormResponse1



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
    detail = None  # Initialize detail to avoid reference errors

    if request.method == 'POST':
        form = NameForm(request.POST)  # Validate submitted data
        if form.is_valid():
            detail = {
                'user_name': form.cleaned_data['user_name'],  # Ensure lowercase field names
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
                'sender': form.cleaned_data['sender'],
                'c_myself': form.cleaned_data['c_myself'],
            }

            # Save data in the database
            response = FormResponse(
                user_name=detail['user_name'],  # Ensure consistency with model field
                subject=detail['subject'],
                message=detail['message'],
                sender=detail['sender'],
                c_myself=detail['c_myself']
            )
            response.save()

            # Redirect to avoid resubmission issues
            return redirect('submission_success', form_id=response.id)  

    else:
        form = NameForm()  # Empty form for GET request

    return render(request, 'uhc/login.html', {'form': form, 'detail': detail})

#def submission_success(request, form_id):
    #response = FormResponse.objects.get(id=form_id)
    #return render(request, 'uhc/success.html', {'response': response})


def get_abi(request):
    detail = None  # Initialize to prevent reference errors
    selected_choice = None  

    if request.method == 'POST':
        form = NameForm1(request.POST)  # Validate submitted data
        if form.is_valid():
            detail = {
                'empanelled': form.cleaned_data['empanelled'],  
                'access': form.cleaned_data['access'],
                'referred': form.cleaned_data['referred'],
            }

            # Save first form's data in FormResponse model
            response = FormResponse1(
                empanelled=detail['empanelled'],  
                access=detail['access'],
                referred=detail['referred'],
            )
            response.save()

            # Handle selection for second form
            selected_choice = form.cleaned_data.get('selection')  
            if selected_choice:
                FormResponse1.objects.create(selection=selected_choice)

            # Redirect to appropriate page
            return redirect('submission_success', form_id=response.id)  

    else:
        form = NameForm1()  # Display empty form on GET request

    return render(request, 'uhc/phc.html', {
        'form': form, 
        'detail': detail, 
        'selected_choice': selected_choice
    })


def submission_success1(request, form_id):
    response = get_object_or_404(FormResponse1, id=form_id)  # Avoids errors if ID doesn't exist
    return render(request, 'uhc/success.html', {'response': response})