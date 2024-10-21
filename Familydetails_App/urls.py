# Familydetails_App/urls.py

from django.urls import path
from .views import FamilyDetailsView

urlpatterns = [
    path('FamilyDetails/', FamilyDetailsView.as_view(), name='family_details_api'),
]
