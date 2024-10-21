from django.db import models

# Create your models here.
# Habbits_Interest_App/models.py

from django.db import models
from UserProfile_App.models import CustomUser

class HabbitsInterest(models.Model):
    #user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='habbits_interest')
    sports = models.CharField(max_length=255)
    movie = models.CharField(max_length=255)
    books = models.CharField(max_length=255)
    travel = models.CharField(max_length=255)
    volunteer_work = models.CharField(max_length=255)
    cooking = models.CharField(max_length=255)
    music = models.CharField(max_length=255)
    writing = models.CharField(max_length=255)
    gaming = models.CharField(max_length=255)
    gardening = models.CharField(max_length=255)

    def __str__(self):
        return f"Hobbies and Interests of {self.user.name} {self.user.surname}"
