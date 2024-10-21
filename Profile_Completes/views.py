# from django.shortcuts import render

# # Profile_Completes/views.py

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from .models import ProfileCompletes
# from .serializers import ProfileCompletesSerializer

# class ProfileCompletesView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         try:
#             profile = request.user.profile_completion
#         except ProfileCompletes.DoesNotExist:
#             return Response({"error": "Profile completion details not found."}, status=status.HTTP_404_NOT_FOUND)

#         serializer = ProfileCompletesSerializer(profile)
#         completion_percentage = profile.calculate_completion_percentage()
#         return Response({
#             'message': f"{request.user.name} {request.user.surname} Details information completed in percentage is= {completion_percentage}%",
#             'data': serializer.data
#         })

#     def post(self, request):
#         user = request.user
#         serializer = ProfileCompletesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=user)
#             return Response({
#                 'message': f"{user.name} {user.surname} Details information",
#                 'data': serializer.data
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# # Create a new file for this API, e.g., Matrimony/views.py

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from UserProfile_App.models import CustomUser
# from ContactUs_App.models import Contact
# from HoroscopeDetails_App.models import HoroscopeDetails
# from EducationDetails_App.models import EducationDetails
# from Familydetails_App.models import FamilyDetails
# from PartnerPreferenceDetails_App.models import PartnerPreferenceDetails
# from Habbits_Interest_App.models import HabbitsInterest

# # class ProfileCompletesView(APIView):
# #     permission_classes = [IsAuthenticated]

# #     def calculate_completion_percentage(self, user):
# #         # Check for each related model's data presence
# #         fields_to_check = [
# #             user.profile_photo,
# #             hasattr(user, 'contactus'),
# #             hasattr(user, 'horoscopedetails'),
# #             hasattr(user, 'educationdetails'),
# #             hasattr(user, 'familydetails'),
# #             hasattr(user, 'partnerpreferencedetails'),
# #             hasattr(user, 'habbits_interest')
# #         ]
# #         completed_fields = sum(1 for field in fields_to_check if field)
# #         total_fields = len(fields_to_check)

# #         # Calculate the completion percentage
# #         return (completed_fields / total_fields) * 100

# #     def get(self, request):
# #         user = request.user
# #         percentage = self.calculate_completion_percentage(user)
        
# #         return Response({
# #             'message': f"{user.name} {user.surname} Details information completed in percentage is= {percentage:.2f}%",
# #             'completion_percentage': percentage
# #         })

# #     def post(self, request):
# #         user = request.user
# #         percentage = self.calculate_completion_percentage(user)

# #         # Return detailed information if all required sections are completed
# #         return Response({
# #             'message': f"{user.name} {user.surname} Details information",
# #             'profile_data': {
# #                 'Profile photo': bool(user.profile_photo),
# #                 'UserProfile completed': hasattr(user, 'userprofile'),
# #                 'ContactUs completed': hasattr(user, 'contactus'),
# #                 'HoroscopeDetails completed': hasattr(user, 'horoscopedetails'),
# #                 'EducationDetails completed': hasattr(user, 'educationdetails'),
# #                 'FamilyDetails completed': hasattr(user, 'familydetails'),
# #                 'PartnerPreferenceDetails completed': hasattr(user, 'partnerpreferencedetails'),
# #                 'Habbits_Interest completed': hasattr(user, 'habbits_interest'),
# #                 'completion_percentage': percentage
# #             }
# #         }, status=status.HTTP_201_CREATED)


# class ProfileCompletesView(APIView):
#     permission_classes = [IsAuthenticated]

#     def calculate_completion_percentage(self, user):
#         # Check if profile_photo exists in UserProfile model related to CustomUser
#         profile_photo_exists = hasattr(user.userprofile, 'profile_photo') and bool(user.userprofile.profile_photo)
        
#         fields_to_check = [
#             profile_photo_exists,
#             hasattr(user, 'contactus'),
#             hasattr(user, 'horoscopedetails'),
#             hasattr(user, 'educationdetails'),
#             hasattr(user, 'familydetails'),
#             hasattr(user, 'partnerpreferencedetails'),
#             hasattr(user, 'habbits_interest')
#         ]
        
#         completed_fields = sum(1 for field in fields_to_check if field)
#         total_fields = len(fields_to_check)
#         return (completed_fields / total_fields) * 100

#     def get(self, request):
#         user = request.user
#         percentage = self.calculate_completion_percentage(user)
        
#         return Response({
#             'message': f"{user.name} {user.surname} Details information completed in percentage is= {percentage:.2f}%",
#             'completion_percentage': percentage
#         })

#     def post(self, request):
#         user = request.user
#         percentage = self.calculate_completion_percentage(user)

#         return Response({
#             'message': f"{user.name} {user.surname} Details information",
#             'profile_data': {
#                 'Profile photo': hasattr(user.userprofile, 'profile_photo') and bool(user.userprofile.profile_photo),
#                 'UserProfile completed': hasattr(user, 'userprofile'),
#                 'ContactUs completed': hasattr(user, 'contactus'),
#                 'HoroscopeDetails completed': hasattr(user, 'horoscopedetails'),
#                 'EducationDetails completed': hasattr(user, 'educationdetails'),
#                 'FamilyDetails completed': hasattr(user, 'familydetails'),
#                 'PartnerPreferenceDetails completed': hasattr(user, 'partnerpreferencedetails'),
#                 'Habbits_Interest completed': hasattr(user, 'habbits_interest'),
#                 'completion_percentage': percentage
#             }
#         }, status=status.HTTP_201_CREATED)




# # ProfileCompletes_App/views.py

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from UserProfile_App.models import CustomUser
# from ContactUs_App.models import Contact
# from HoroscopeDetails_App.models import HoroscopeDetails
# from EducationDetails_App.models import EducationDetails
# from Familydetails_App.models import FamilyDetails
# from PartnerPreferenceDetails_App.models import PartnerPreferenceDetails
# from Habbits_Interest_App.models import HabbitsInterest

# class ProfileCompletesView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user = request.user
        
#         # Initialize completed fields count
#         completed_fields = 0
#         total_fields = 6  # Total number of apps considered

#         # Check if user profile is complete
#         if hasattr(user, 'userprofile'):
#             completed_fields += 1  # UserProfile  # +=1

#         if hasattr(user, 'contactus'):
#             completed_fields += 1  # ContactUs 6

#         if hasattr(user, 'horoscopedetails'):
#             completed_fields += 1  # HoroscopeDetails 12

#         if hasattr(user, 'educationdetails'):
#             completed_fields += 1  # EducationDetails  8

#         if hasattr(user, 'familydetails'):
#             completed_fields += 1  # FamilyDetails  15

#         if hasattr(user, 'partnerpreferencedetails'):
#             completed_fields = 1 # PartnerPreferenceDetails  13

#         if hasattr(user, 'habbits_interest'):
#             completed_fields += 1    # HabbitsInterest  10

#         # Calculate completion percentage
#         completion_percentage = (completed_fields / total_fields) * 100
        
#         return Response({
#             'message': f"{user.name} {user.surname} Details information completed in percentage is = {completion_percentage:.2f}%"
#         })

#     def post(self, request):
#         user = request.user
        
#         # Simulating the post request for profile completion. 
#         # Here you might want to save data but as per your requirement, we are only calculating.
#         return Response({
#             'message': f"{user.name} {user.surname} Profile completion details submitted."
#         }, status=status.HTTP_201_CREATED)


# ProfileCompletes_App/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from UserProfile_App.models import CustomUser
from ContactUs_App.models import Contact
from HoroscopeDetails_App.models import HoroscopeDetails
from EducationDetails_App.models import EducationDetails
from Familydetails_App.models import FamilyDetails
from PartnerPreferenceDetails_App.models import PartnerPreferenceDetails
from Habbits_Interest_App.models import HabbitsInterest

class ProfileCompletesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        
        # Initialize completed fields count
        completed_fields = 0
        total_fields = 7  # Total number of apps considered

        # Check if user profile is complete
        if hasattr(user, 'userprofile') and all([user.userprofile.name, user.userprofile.surname]):
            completed_fields += 1  # UserProfile

        if hasattr(user, 'contactus') and all([user.contactus.mobile_number, user.contactus.email, user.contactus.convenient_time_to_call]):
            completed_fields += 1  # ContactUs

        if hasattr(user, 'horoscopedetails') and all([user.horoscopedetails.moon_sign, user.horoscopedetails.place_of_birth]):
            completed_fields += 1  # HoroscopeDetails

        if hasattr(user, 'educationdetails') and all([user.educationdetails.qualification, user.educationdetails.occupations]):
            completed_fields += 1  # EducationDetails

        if hasattr(user, 'familydetails') and all([user.familydetails.family_status, user.familydetails.mother_name]):
            completed_fields += 1  # FamilyDetails

        if hasattr(user, 'partnerpreferencedetails') and all([user.partnerpreferencedetails.religion, user.partnerpreferencedetails.height_from]):
            completed_fields += 1  # PartnerPreferenceDetails

        if hasattr(user, 'habbits_interest') and all([user.habbits_interest.sports, user.habbits_interest.cooking]):
            completed_fields += 1  # HabbitsInterest

        # Calculate completion percentage
        completion_percentage = (completed_fields / total_fields) * 100
        
        return Response({
            'message': f"{user.name} {user.surname} Details information completed in percentage is = {completion_percentage:.2f}%"
        })
