from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.exceptions import SuspiciousOperation

from .models import UserAccount
from .forms import RegisterForm


def userRegister(request):
  context = {}
  
  if(request.user.is_authenticated):
      return redirect('homepage')
  
  if(request.method == 'POST'):
    
    form = RegisterForm(request.POST)
    if(form.is_valid()):
        
        #Validating form and data using DjangoValidation
        form.save()
        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')

        #Attempt login
        account = authenticate(email=email, password=raw_password)
        login(request, account)
        return redirect('homepage')

    else:
        context['registration_form'] = form
  
  # Reached if request is not POST (GET)
  else:
    form = RegisterForm()
    context['registration_form'] = form

  return render(request, 'UserAccounts/register.html', context)