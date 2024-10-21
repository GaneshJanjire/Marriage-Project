from django.db import models

# Create your models here.
# HoroscopeDetails_App/models.py

from django.db import models
from UserProfile_App.models import CustomUser

class HoroscopeDetails(models.Model):
    #user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='horoscope_details')
    moon_sign = models.CharField(max_length=20)
    star = models.CharField(max_length=20)
    gotra = models.CharField(max_length=50)
    manglik = models.CharField(max_length=100)
    shani = models.CharField(max_length=100)
    horoscope_match = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=100)
    place_of_country = models.CharField(max_length=100)
    hours = models.PositiveIntegerField()
    minutes = models.PositiveIntegerField()
    seconds = models.PositiveIntegerField()
    AM_PM = models.CharField(max_length=2, choices=[('AM', 'AM'), ('PM', 'PM')])

    def __str__(self):
        return f"Horoscope Details of {self.user.name} {self.user.surname}"
