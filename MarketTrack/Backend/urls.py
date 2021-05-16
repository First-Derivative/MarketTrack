from django.urls import path
from .views import *

urlpatterns = [
  path("search/<str:query>", search_api),
  path("get/tracked_items", getTrackedItems, name="getTracked_api"),
  path("get/item_dataset/<int:item_id>", getItemDataset, name="getItemDataset_api"),
  path("post/tracked_item/", addTrackedItem, name="postTracked_api"),
  path("delete/tracked_item/<int:item_id>", deleteTrackedItem, name="deleteTrackedItems_api"),
]