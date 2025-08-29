from django.db import models
from users.models import CustomUser
# Create your models here.

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