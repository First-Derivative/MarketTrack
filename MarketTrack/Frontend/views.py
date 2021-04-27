# from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required, user_passes_test

def homepage_view(request):
 
  return render(request, 'Frontend/homepage.html', {})