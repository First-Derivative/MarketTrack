from django.urls import path
from .views import *

urlpatterns = [

    path('', homepage_view, name="homepage"),    
    path('collections', collections_view, name="collections_page"),
    path('tracked', tracked_view, name="tracked_page"),

]