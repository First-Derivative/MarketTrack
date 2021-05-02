from django.contrib import admin
from Frontend.models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "source", "price", "timestamp")
    search_fields = ("id","name", "price")

class TrackedAdmin(admin.ModelAdmin):
    list_display = ("id", "item", "user")
    search_fields = ("id","item", "user")

# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Tracked, TrackedAdmin)