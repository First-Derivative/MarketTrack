from django.urls import path
from .views import *

urlpatterns = [

    path('', homepage_view, name="homepage"),    
    # path('/<str:user>/collections', collections_view, name="collections_page"),
    # path('/<str:user>/tracked', trackedpage_view, name="tracked_page")

]