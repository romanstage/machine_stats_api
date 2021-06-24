from django.contrib import admin
from .models import Stats


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'cpu_usage','ram_usage','gpu_usage', "time")
    list_display_links = ("time",)


