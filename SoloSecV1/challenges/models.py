from django.db import models
from users.models import CustomUser
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)                     # Room name
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Owner of the room
    difficulty = models.CharField(max_length=10, choices=[
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ])
    created_at = models.DateTimeField(auto_now_add=True)         # Timestamp

    def __str__(self):
        return self.name
 
class Challenge(models.Model):
    CATEGORY_CHOICES = [
        ('Web', 'Web'),
        ('Crypto', 'Crypto'),
        ('Forensics', 'Forensics'),
        ('Pwn', 'Pwn'),
        ('Misc', 'Misc')
    ]

    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    description = models.TextField()
    points = models.IntegerField(default=0)
    flag = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.title} - {self.category} - {self.difficulty}"