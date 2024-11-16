# backend/core/admin.py

from django.contrib import admin
from .models import CoreModel

@admin.register(CoreModel)
class CoreModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
