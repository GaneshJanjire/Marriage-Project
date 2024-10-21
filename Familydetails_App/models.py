from django.db import models

# Create your models here.
# Familydetails_App/models.py

from django.db import models
from UserProfile_App.models import CustomUser

class FamilyDetails(models.Model):

    PARENTS_CHOICES = (
        ('My parents will stay with me after marriage', 'My parents will stay with me after marriage'),
        ('My parents will not stay with me after marriage', 'My parents will not stay with me after marriage'),
        ('Dont wish to specify', 'Dont wish to specify'),
    )

    #user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='family_details')
    looking_for = models.CharField(max_length=50, choices=PARENTS_CHOICES)
    family_values = models.CharField(max_length=100)
    family_type = models.CharField(max_length=100)
    family_status = models.CharField(max_length=100)
    no_of_brothers = models.PositiveIntegerField()
    no_of_brothers_married = models.PositiveIntegerField()
    no_of_sisters = models.PositiveIntegerField()
    no_of_sisters_married = models.PositiveIntegerField()
    mother_tounge = models.CharField(max_length=50)
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    family_wealth = models.CharField(max_length=100)
    about_family = models.TextField()

    def __str__(self):
        return f"Family Details of {self.user.name} {self.user.surname}"
