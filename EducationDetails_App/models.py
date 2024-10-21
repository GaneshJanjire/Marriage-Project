from django.db import models

# Create your models here.
# EducationDetails_App/models.py

from django.db import models
from UserProfile_App.models import CustomUser

class EducationDetails(models.Model):
    #user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='education_details')
    looking_for = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    occupations = models.CharField(max_length=100)
    occupation_details = models.TextField()
    annual_income = models.CharField(max_length=20)
    employed_in = models.CharField(max_length=50)
    working_location = models.CharField(max_length=100)
    special_cases = models.TextField()

    def __str__(self):
        return f"Education Details of {self.user.name} {self.user.surname}"
