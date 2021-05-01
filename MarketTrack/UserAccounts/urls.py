from django.urls import path
from .views import *

urlpatterns = [
  path('registrations/', userRegister, name="user_registration"),
]