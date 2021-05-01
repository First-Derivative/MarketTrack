from django.urls import path
from .views import *

urlpatterns = [

  path('/api/search/<str:query>', search_api),    
  # path('/<str:user>/collections', collections_view, name="user_collections"),
  # path('/<str:user>/tracked', tracked_view, name="user_tracked")

]