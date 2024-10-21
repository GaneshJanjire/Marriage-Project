# EducationDetails_App/serializers.py

from rest_framework import serializers
from .models import EducationDetails

class EducationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDetails
        fields = [
            'looking_for', 'qualification', 'occupations', 'occupation_details', 
            'annual_income', 'employed_in', 'working_location', 'special_cases'
        ]
