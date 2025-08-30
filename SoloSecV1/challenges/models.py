from django.db import models

DIFFICULTY_POINTS = {"Easy": 10, "Medium": 20, "Hard": 30}

class Room(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=10, choices=[
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

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

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    description = models.TextField()
    points = models.IntegerField(default=0)
    flag = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.points:
            self.points = DIFFICULTY_POINTS.get(self.difficulty, 0)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
