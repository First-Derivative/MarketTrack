from django.contrib import admin
from Frontend.models import *

class ItemAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "price", "source", "abstract_source", "timestamp")
  search_fields = ("id","name", "price")

class TrackedAdmin(admin.ModelAdmin):
  list_display = ("id", "item", "user")
  search_fields = ("id","item", "user")

class PermanentTrackAdmin(admin.ModelAdmin):
  list_display = ("id", "price", "source","abstract_source", "stock_bool", "timestamp")
  search_fields = ("id", "")

# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Tracked, TrackedAdmin)
admin.site.register(PermanentTrack, PermanentTrackAdmin)