from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required, user_passes_test

def search_api(request, query):
  return HttpResponse(status=200)

@login_required
def getTrackedItems(request):
  if(request.method == "GET"):
    return HttpResponse(status=200)
  return HttpResponseBadRequest("Invalid Request")

# 404 error handler view
def error_handler(request):
  return HttpResponseBadRequest("Invalid Resource")