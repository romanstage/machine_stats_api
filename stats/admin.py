from django.contrib import admin
from .models import CPU_usage


@admin.register(CPU_usage)
class CPU_usageAdmin(admin.ModelAdmin):
    list_display = ('id', 'usage', "time")
    list_display_links = ("time",)


