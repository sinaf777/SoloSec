from django.db import models
from django.contrib.auth.models import AbstractUser
from challenges.models import Challenge
# Create your models here.

class CustomUser(AbstractUser):
    score = models.IntegerField(default=0)
    solved = models.ManyToManyField('challenges.Challenge', blank=True, related_name='solved_by')

    def __str__(self):
        return self.username

class Badge(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    min_score = models.IntegerField()
    icon = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name
    