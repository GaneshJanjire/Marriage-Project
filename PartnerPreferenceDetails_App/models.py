from django.db import models

# Create your models here.
# PartnerPreferenceDetails_App/models.py

from django.db import models
from UserProfile_App.models import CustomUser

class PartnerPreferenceDetails(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
    )

    #user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='partner_preference')
    looking_for = models.CharField(max_length=20, choices=GENDER_CHOICES)
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    height_from = models.DecimalField(max_digits=4, decimal_places=2)
    height_to = models.DecimalField(max_digits=4, decimal_places=2)
    religion = models.CharField(max_length=100)
    caste = models.CharField(max_length=100)
    complexion = models.CharField(max_length=100)
    residency_status = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    partner_expectations = models.TextField()

    def __str__(self):
        return f"Partner Preferences of {self.user.name} {self.user.surname}"
