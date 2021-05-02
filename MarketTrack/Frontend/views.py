# from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required, user_passes_test

def homepage_view(request):
  if(request.method == "GET"):
    return render(request, "Frontend/homepage.html", {})
  return HttpResponseBadRequest("Invalid Request")

def collections_view(request):
  if(request.method == "GET"):
    return render(request, "Frontend/collections.html", {})
  return HttpResponseBadRequest("Invalid Request")

def tracked_view(request):
  if(request.method == "GET"):
    return render(request, "Frontend/tracked.html", {})
  return HttpResponseBadRequest("Invalid Request")