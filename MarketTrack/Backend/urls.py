from django.urls import path
from .views import *

urlpatterns = [
  path("search/<str:query>", search_api),
  path("get/tracked_items", getTrackedItems),
  # path("get/collections", getColelctions),
]