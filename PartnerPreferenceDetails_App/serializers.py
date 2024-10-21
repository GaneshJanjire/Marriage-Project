# PartnerPreferenceDetails_App/serializers.py

from rest_framework import serializers
from .models import PartnerPreferenceDetails

class PartnerPreferenceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerPreferenceDetails
        fields = [
            'looking_for', 'age_from', 'age_to', 'height_from', 'height_to', 'religion', 'caste', 'complexion',
            'residency_status', 'country', 'education', 'occupation', 'partner_expectations'
        ]
