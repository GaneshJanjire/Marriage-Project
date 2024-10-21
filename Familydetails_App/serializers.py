# Familydetails_App/serializers.py

from rest_framework import serializers
from .models import FamilyDetails

class FamilyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyDetails
        fields = [
            'looking_for', 'family_values', 'family_type', 'family_status', 'no_of_brothers', 'no_of_brothers_married',
            'no_of_sisters', 'no_of_sisters_married', 'mother_tounge', 'father_name', 'father_occupation',
            'mother_name', 'mother_occupation', 'family_wealth', 'about_family'
        ]
