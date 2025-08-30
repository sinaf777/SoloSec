from django.db import models
from challenges.models import Challenge
# Create your models here.
class Room(models.Model):
    DIFFICULTY_CHOICES = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField(help_text="Supports Markdown")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    points = models.IntegerField(default=0)

    # Many-to-many relationship to Challenges
    challenges = models.ManyToManyField(Challenge, related_name="rooms")

    def __str__(self):
        return self.title