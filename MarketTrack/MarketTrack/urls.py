from django.contrib import admin
from django.urls import include ,path

urlpatterns = [
  path("admin/", admin.site.urls),

  path("", include("Frontend.urls")),

  path("api/",include("Backend.urls")),

  path("user/", include("UserAccounts.urls"))
]
