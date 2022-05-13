from django.contrib import admin

# Register your models here.
from .models import User


@admin.register(User)
class PostModelAdmin(admin.ModelAdmin):
    pass