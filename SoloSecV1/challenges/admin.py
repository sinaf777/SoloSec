from django.contrib import admin
from .models import Challenge
from .models import Room
# Register your models here.
@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "difficulty", "points")

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at", "difficulty")