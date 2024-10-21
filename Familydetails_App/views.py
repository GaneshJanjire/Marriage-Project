from django.shortcuts import render

# Create your views here.
# Familydetails_App/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import FamilyDetails
from .serializers import FamilyDetailsSerializer

class FamilyDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            family_details = request.user.family_details
        except FamilyDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Family details not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FamilyDetailsSerializer(family_details)
        return Response({
            'message': f"{request.user.name} {request.user.surname} Family Details information",
            'data': serializer.data
        })

    def post(self, request):
        user = request.user
        serializer = FamilyDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({
                'message': f"{user.name} {user.surname} Family Details information",
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            family_details = request.user.family_details
        except FamilyDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Family details not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = FamilyDetailsSerializer(family_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{request.user.name} {request.user.surname} Family Details updated successfully",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            family_details = request.user.family_details
        except FamilyDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Family details not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = FamilyDetailsSerializer(family_details, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{request.user.name} {request.user.surname} Family Details updated successfully",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            family_details = request.user.family_details
        except FamilyDetails.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname}Family details not found."}, status=status.HTTP_404_NOT_FOUND)

        family_details.delete()
        return Response({
            'message': f"{request.user.name} {request.user.surname} Family Details deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
