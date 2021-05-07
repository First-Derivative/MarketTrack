from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required, user_passes_test

from UserAccounts.models import UserAccount
from Frontend.models import *

def search_api(request, query):
  return HttpResponse(status=200)

def resolveAbstractSource(item):
  choice = item.abstract_source
  for choices in AbstractSourceChoice:
    if(choice == choices):
      return choices.label

def serializeItem(item):
  serializedItem = {}
  serializedItem["id"] = item.id
  serializedItem["name"] = item.name
  serializedItem["source"] = item.source
  serializedItem["abstract_source"] = resolveAbstractSource(item)
  serializedItem["price"] = item.price
  if(item.stock_bool):
    serializedItem["stock_bool"] = "Yes"
  else:
    serializedItem["stock_bool"] = "No"
  serializedItem["stock_no"] = item.stock_no
  serializedItem["timestamp"] = item.timestamp.strftime('%H:%M %d %B, %Y')

  return serializedItem

def serializeItemDataset(itemSet):
  response = {"dataset":[], "label":[]}
  for item in itemSet:
    response["dataset"].append(item.price)
    response["label"].append(item.timestamp.strftime('%H:%M,%d-%B-%Y'))
  return response

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
        return JsonResponse({"noItem": "true"})
    
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
  return HttpResponseBadRequest("Invalid Request, not GET")


def addTrackedItem(request):
  if(request.method == "POST"):
    if(request.user.is_anonymous):
      return JsonResponse({"error":"Only users can track items! Register an account or log in to start tracking"})
    post = request.POST
    content = post.get("content")
    print(content)
    return HttpResponse(status=200)
  return HttpResponseBadRequest("Invalid Request, not POST")

@login_required
def deleteTrackedItem(request, item_id):
  if(request.method == "DELETE"):
    user = request.user
    try:
      tracked_item = Tracked.objects.get(id=item_id)
      tracked_item.delete()
      return HttpResponse(status=200)
    except Tracked.DoesNotExist:
      return HttpResponseBadRequest("Invalid Item ID")
  return HttpResponseBadRequest("Invalid Request, not DELETE")

@login_required
def getItemDataset(request, item_id):
  if(request.method == "GET"):
    try:
      item_queryset = PermanentTrack.objects.all().filter(item=item_id).order_by('timestamp')
      response = serializeItemDataset(item_queryset)
      return JsonResponse({"itemSet": response})
    except PermanentTrack.DoesNotExist:
      return HttpResponseBadRequest("Invalid Item ID")
  return HttpResponseBadRequest("Invalid Request, not GET")

# 404 error handler view
def error_handler(request):
  return HttpResponseBadRequest("Invalid Resource")

def testView(request):
  if(request.user.is_anonymous):
    print("ANONYMOUS")
  return HttpResponse(status=200)
