from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('', homepage_view, name="homepage"),    
    # path('/<str:user>/collections', collections_view, name="user_collections"),
    # path('/<str:user>/tracked', tracked_view, name="user_tracked")

]