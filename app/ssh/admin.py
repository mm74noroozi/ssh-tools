from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display=('name','address','port')