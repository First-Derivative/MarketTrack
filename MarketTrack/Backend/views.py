from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required, user_passes_test

from UserAccounts.models import UserAccount
from Frontend.models import *

def search_api(request, query):
  return HttpResponse(status=200)

def serializeItem(item):
  serializedItem = {}
  serializedItem["name"] = item.name
  serializedItem["source"] = item.source
  serializedItem["price"] = item.price
  serializedItem["stock_bool"] = item.stock_bool
  serializedItem["stock_no"] = item.stock_no
  serializedItem["timestamp"] = item.timestamp

  return serializedItem

def getTrackedItems(request):
  if(request.method == "GET"):
    if(not request.user.is_anonymous):
      
      user = request.user
      json_tracked = []
      tracked_query = Tracked.objects.filter(user=user)
      
      if(tracked_query.exists()):
        
        for tracked_items in tracked_query:
          obj = serializeItem(tracked_items.item)
          json_tracked.append(obj)
        return JsonResponse({"tracked_items": json_tracked})
      
      else:
        return JsonResponse({"noItems": "true"})
    
    else:
      return JsonResponse({"noUser": "true"})
  return HttpResponseBadRequest("Invalid Request")

def getCollections(request):
  if(request.method == "GET"):
    
    if(not request.user.is_anonymous):
      user = request.user
      json_collections = []
      collection_query = Collection.objects.filter(user=user)
      
      if(collection_query.exists()):
        
        for collection in collection_query:
          obj = {"name":collection.name}
          i = 0
          for collection_item in CollectionItems.objects.filter(collection=collection):
            i+= 1
            obj["item_{}".format(i)] = serializeItem(collection_item.item)
          json_collections.append(obj)
          
        return JsonResponse({"collections": json_collections})
      else:
        return JsonResponse({"noCollections": "true"})
    else:
      return JsonResponse({"noUser": "true"})
  return HttpResponseBadRequest("Invalid Request")

# 404 error handler view
def error_handler(request):
  return HttpResponseBadRequest("Invalid Resource")

def testView(request):
  if(request.user.is_anonymous):
    print("ANONYMOUS")
  return HttpResponse(status=200)
