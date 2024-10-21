from django.shortcuts import render

# Create your views here.
# HoroscopeDetails_App/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import HoroscopeDetails
from .serializers import HoroscopeDetailsSerializer
from UserProfile_App.models import CustomUser

class HoroscopeDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            horoscope = request.user.horoscope_details
        except HoroscopeDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Horoscope details not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = HoroscopeDetailsSerializer(horoscope)
        return Response({
            'message': f"{request.user.name} {request.user.surname} Horoscope information",
            'data': serializer.data
        })

    def post(self, request):
        user = request.user
        serializer = HoroscopeDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({
                'message': f"{user.name} {user.surname} Horoscope information",
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            horoscope = request.user.horoscope_details
        except HoroscopeDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Horoscope details not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HoroscopeDetailsSerializer(horoscope, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{request.user.name} {request.user.surname} Horoscope Details updated successfully",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            horoscope = request.user.horoscope_details
        except HoroscopeDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Horoscope details not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HoroscopeDetailsSerializer(horoscope, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{request.user.name} {request.user.surname} Horoscope Details updated successfully",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            horoscope = request.user.horoscope_details
        except HoroscopeDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Horoscope details not found."}, status=status.HTTP_404_NOT_FOUND)

        horoscope.delete()
        return Response({
            'message': f"{request.user.name} {request.user.surname} Horoscope Details deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
