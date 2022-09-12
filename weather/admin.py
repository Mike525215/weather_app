from django.contrib import admin
from .models import *
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id']
    ordering = ['id']
admin.site.register(City, CityAdmin)