from django.contrib import admin
from .models import UserMod


@admin.register(UserMod)
class AdminUserMod(admin.ModelAdmin):
    pass