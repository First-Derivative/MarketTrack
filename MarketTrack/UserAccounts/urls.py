from django.urls import path
from .views import *

urlpatterns = [
  path('registrations/', userRegister, name="user_registration"),
  path('login/', userLogin, name="user_login")
]