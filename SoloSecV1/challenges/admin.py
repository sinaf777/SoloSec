from django.contrib import admin
from .models import Challenge
# Register your models here.
@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "difficulty", "points")