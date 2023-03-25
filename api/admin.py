from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Notification, Location, HelpRequest

# Register your models here.

admin.site.register(Notification)
admin.site.register(HelpRequest)

@admin.register(Location)
class LocationAdmin(OSMGeoAdmin):
    list_display = ('user', 'location', 'date', 'is_active')
    default_lon = 77.5946
    default_lat = 12.9716
    default_zoom = 10