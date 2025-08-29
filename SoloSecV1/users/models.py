from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    score = models.IntegerField(default=0)
    solved = models.ManyToManyField('challenges.Challenge', blank=True)

    def __str__(self):
        return self.username