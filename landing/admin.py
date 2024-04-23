from . import models
from django.contrib import admin


@admin.register(models.Leave)
class LeaveAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ["status", "user"]
    list_display = ["title", "user", "status"]


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "created_at", "updated_at"]
