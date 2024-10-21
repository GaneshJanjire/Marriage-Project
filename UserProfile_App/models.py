from django.db import models

# Create your models here.
from django.db import models

# UserProfile_App/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# UserProfile_App/models.py


from django.db import models
from django.contrib.auth.models import AbstractUser
# UserProfile_App/models.py


from rest_framework_simplejwt.tokens import RefreshToken

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    Email_ID = models.EmailField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    age = models.PositiveIntegerField()
    height = models.FloatField()
    blood_group = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.TextField()
    zipcode = models.CharField(max_length=10)
    profile_created_by = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=20)
    education = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    religion = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    subcaste = models.CharField(max_length=50)
    about_yourself = models.TextField()
    image = models.ImageField(upload_to='media/')

    
    # Customize the related_name for user_permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',  # Change this to avoid conflict
        help_text='Specific permissions for this user.',
        related_query_name='custom_user',
    )

    def get_token(self):
        refresh = RefreshToken.for_user(self)
        # Optionally add custom claims to the token
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

