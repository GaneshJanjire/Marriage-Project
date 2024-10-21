# # Profile_Completes/models.py

# from django.db import models
# from UserProfile_App.models import CustomUser

# class ProfileCompletes(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile_completion')
#     profile_photo = models.FileField(upload_to='media', null=True)
#     basic_details_completed = models.BooleanField(default=False)
#     education_details_completed = models.BooleanField(default=False)
#     horoscope_details_completed = models.BooleanField(default=False)
#     family_details_completed = models.BooleanField(default=False)
#     partner_preference_details_completed = models.BooleanField(default=False)
#     habbits_interests_details_completed = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Profile Completion for {self.user.name} {self.user.surname}"

# #     def calculate_completion_percentage(self):
# #         fields = [
# #             self.profile_photo,
# #             self.basic_details_completed,
# #             self.education_details_completed,
# #             self.horoscope_details_completed,
# #             self.family_details_completed,
# #             self.partner_preference_details_completed,
# #             self.habbits_interests_details_completed,
# #         ]
# #         return sum(fields) / len(fields) * 100

# # # UserProfile_App/models.py

# # class ProfileCompleteness(models.Model):
# #     # fields as before...

#     def calculate_completion_percentage(self):
#         total_fields = 8  # Adjust if needed based on required fields
#         completed_fields = sum([
#             self.profile_photo, self.user_profile_details, self.contact_details, 
#             self.horoscope_details, self.education_details, self.family_details, 
#             self.partner_preferences, self.habbits_interest
#         ])
#         return int((completed_fields / total_fields) * 100)
