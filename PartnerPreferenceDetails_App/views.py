from django.shortcuts import render

# Create your views here.
# PartnerPreferenceDetails_App/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import PartnerPreferenceDetails
from .serializers import PartnerPreferenceDetailsSerializer

class PartnerPreferenceDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            partner_preferences = request.user.partner_preference
        except PartnerPreferenceDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Partner preference details not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PartnerPreferenceDetailsSerializer(partner_preferences)
        return Response({
            'message': f"{request.user.name} {request.user.surname} Partner Preference Details information",
            'data': serializer.data
        })

    def post(self, request):
        user = request.user
        serializer = PartnerPreferenceDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({
                'message': f"{user.name} {user.surname} Partner Preference Details information",
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            partner_preferences = request.user.partner_preference
        except PartnerPreferenceDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Partner preference details not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PartnerPreferenceDetailsSerializer(partner_preferences, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{request.user.name} {request.user.surname} Partner Preference Details updated successfully",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            partner_preferences = request.user.partner_preference
        except PartnerPreferenceDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Partner preference details not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PartnerPreferenceDetailsSerializer(partner_preferences, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{request.user.name} {request.user.surname} Partner Preference Details updated successfully",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            partner_preferences = request.user.partner_preference
        except PartnerPreferenceDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Partner preference details not found."}, status=status.HTTP_404_NOT_FOUND)

        partner_preferences.delete()
        return Response({
            'message': f"{request.user.name} {request.user.surname} Partner Preference Details deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
