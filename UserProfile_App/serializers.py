# UserProfile_App/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


# UserProfile_App/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'surname', 'Email_ID', 'mobile_number', 'date_of_birth', 'age', 'height',
                  'blood_group', 'gender', 'country', 'state', 'city', 'address', 'zipcode', 'profile_created_by',
                  'marital_status', 'education', 'occupation', 'income', 'religion', 'caste', 'subcaste', 'about_yourself', 'image']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
