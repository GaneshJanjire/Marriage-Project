# Habbits_Interest_App/serializers.py

from rest_framework import serializers
from .models import HabbitsInterest

class HabbitsInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabbitsInterest
        fields = [
            'sports', 'movie', 'books', 'travel', 'volunteer_work', 'cooking', 'music', 
            'writing', 'gaming', 'gardening'
        ]
