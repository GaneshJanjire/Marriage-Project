# ContactUs_App/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from .serializers import ContactSerializer
from UserProfile_App.models import CustomUser



class ContactView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            contact = request.user.contact_info
        except Contact.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Contact information not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ContactSerializer(contact)
        return Response({
            'message': f"{request.user.name} {request.user.surname} information",
            'data': serializer.data
        })

    def post(self, request):
        user = request.user
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({
                'message': f"{user.name} {user.surname} information",
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            contact = request.user.contact_info
        except Contact.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Contact information not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{request.user.name} {request.user.surname} data updated successfully",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            contact = request.user.contact_info
        except Contact.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Contact information not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{request.user.name} {request.user.surname} data updated successfully",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            contact = request.user.contact_info
        except Contact.DoesNotExist:
            return Response({"error": f"{request.user.name} {request.user.surname} Contact information not found."}, status=status.HTTP_404_NOT_FOUND)

        contact.delete()
        return Response({
            'message': f"{request.user.name} {request.user.surname} data deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
