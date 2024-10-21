# ContactUs_App/serializers.py

from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['mobile_number', 'alternative_mobile_number', 'convenient_time_to_call', 
                  'email', 'show_permanent_address', 'show_working_address']
