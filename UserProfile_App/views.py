from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# UserProfile_App/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# UserProfile_App/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# UserProfile_App/views.py

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = user.get_token()  # Use the get_token method here

            name = user.name
            surname = user.surname

            return Response({
                'message': f"{name} {surname} registration successful.",
                'refresh': token['refresh'],
                'access': token['access'],
                'user_data': {
                    'username': user.username,
                    'email': user.email,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)

#             # Prepare the response message with name and surname
#             name = user.name
#             surname = user.surname

#             return Response({
#                 'message': f"{name} {surname} registration successful.",
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token)
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            try:
                user = CustomUser.objects.get(username=username)
                if user.check_password(password):
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'message': f"{user.name} {user.surname} logged in successfully",
                        'data': {
                            'refresh': str(refresh),
                            'access': str(refresh.access_token),
                            'user_data': {
                                'username': user.username,
                                'email': user.email,
                                # Add other fields you want to show
                            }
                        }
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({"error": f"{username} is not registered"}, status=status.HTTP_401_UNAUTHORIZED)
            except CustomUser.DoesNotExist:
                return Response({"error": f"{username} is not registered"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response({
            'message': f"{user.name} {user.surname} all information",
            'data': serializer.data
        })

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{user.name} {user.surname} data updated successfully",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        username = user.username  # Get the username for the message
        user.delete()
        return Response({
            'message': f"{username} data deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)  # Partial update
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"{user.name} {user.surname} data updated successfully (partial update)",
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)