from django.shortcuts import render

# Create your views here.
# EducationDetails_App/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import EducationDetails
from .serializers import EducationDetailsSerializer

class EducationDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            education_details = request.user.education_details
        except EducationDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Education details not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EducationDetailsSerializer(education_details)
        return Response({
            'message': f"{request.user.name} {request.user.surname} Educational Details information",
            'data': serializer.data
        })

    def post(self, request):
        user = request.user
        serializer = EducationDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({
                'message': f"{user.name} {user.surname} Educational Details information",
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            education_details = request.user.education_details
        except EducationDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Education details not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = EducationDetailsSerializer(education_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{request.user.name} {request.user.surname} Education Details updated successfully",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            education_details = request.user.education_details
        except EducationDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Education details not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = EducationDetailsSerializer(education_details, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{request.user.name} {request.user.surname} Education Details updated successfully",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            education_details = request.user.education_details
        except EducationDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Education details not found."}, status=status.HTTP_404_NOT_FOUND)

        education_details.delete()
        return Response({
            'message': f"{request.user.name} {request.user.surname} Educational Details deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
