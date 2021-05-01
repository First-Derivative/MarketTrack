from django.contrib import admin
from django.urls import include ,path
# from django.conf.urls.defaults import handler404, handler500

urlpatterns = [
  path("admin/", admin.site.urls),

  path("", include("Frontend.urls")),

  path("api/",include("Backend.urls")),

  path("user/", include("UserAccounts.urls"))
]

# handler404 = "Backend.views.error_handler"
