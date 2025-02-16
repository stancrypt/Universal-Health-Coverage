from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .chart import calculate
from .login import NameForm
from .models import FormResponse



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

def submission_success(request, form_id):
    response = FormResponse.objects.get(id=form_id)
    return render(request, 'uhc/success.html', {'response': response})