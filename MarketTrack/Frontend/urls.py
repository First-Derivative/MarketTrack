from django.urls import path
from .views import *

urlpatterns = [

    path('', homepage_view, name="homepage"),    
    path('tracked', tracked_view, name="tracked_page"),
    path('stats', stats_view, name="stats_page"),

]