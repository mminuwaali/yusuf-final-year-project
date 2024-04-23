from . import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(models.User)
class UserAdmin(BaseUserAdmin): ...


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ["department"]
    search_fields = ["employee__username", "department"]
    list_display = ["employee", "department", "performance"]
