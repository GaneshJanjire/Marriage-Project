from django.shortcuts import render

# Create your views here.
# Habbits_Interest_App/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import HabbitsInterest
from .serializers import HabbitsInterestSerializer

class HabbitsInterestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            habbits_interest = request.user.habbits_interest
        except HabbitsInterest.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Hobbies and interests details not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HabbitsInterestSerializer(habbits_interest)
        return Response({
            'message': f"{request.user.name} {request.user.surname} Hobbits and Interest Details information",
            'data': serializer.data
        })

    def post(self, request):
        user = request.user
        serializer = HabbitsInterestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({
                'message': f"{user.name} {user.surname} Hobbits and Interest Details information",
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            habbits_interest = request.user.habbits_interest
        except HabbitsInterest.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Hobbies and interests details not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HabbitsInterestSerializer(habbits_interest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{request.user.name} {request.user.surname} Hobbits and Interest Details updated successfully",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            habbits_interest = request.user.habbits_interest
        except HabbitsInterest.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Hobbies and interests details not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HabbitsInterestSerializer(habbits_interest, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{request.user.name} {request.user.surname} Hobbits and Interest Details updated successfully",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            habbits_interest = request.user.habbits_interest
        except HabbitsInterest.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Hobbies and interests details not found."}, status=status.HTTP_404_NOT_FOUND)

        habbits_interest.delete()
        return Response({
            'message': f"{request.user.name} {request.user.surname} Hobbits and Interest Details deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
