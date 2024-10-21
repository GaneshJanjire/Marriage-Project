# ContactUs_App/models.py

from django.db import models
from UserProfile_App.models import CustomUser

class Contact(models.Model):
    #user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='contact_info')
    mobile_number = models.CharField(max_length=15)
    alternative_mobile_number = models.CharField(max_length=15, blank=True, null=True)
    convenient_time_to_call = models.CharField(max_length=50)
    email = models.EmailField()
    show_permanent_address = models.TextField()
    show_working_address = models.TextField()

    def __str__(self):
        return f"Contact Info of {self.user.name} {self.user.surname}"
