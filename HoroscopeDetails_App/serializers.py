# HoroscopeDetails_App/serializers.py

from rest_framework import serializers
from .models import HoroscopeDetails

class HoroscopeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoroscopeDetails
        fields = [
            'moon_sign', 'star', 'gotra', 'manglik', 'shani', 'horoscope_match', 
            'place_of_birth', 'place_of_country', 'hours', 'minutes', 'seconds', 'AM_PM'
        ]
