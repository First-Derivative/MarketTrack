from django.urls import path
from .views import *

urlpatterns = [
  path("search/<str:query>", search_api),
  path("get/tracked_items", getTrackedItems, name="getTracked_api"),
  path("get/collections", getCollections, name="getCollections_api"),
  path("tester", testView)
]