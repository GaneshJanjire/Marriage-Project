# PartnerPreferenceDetails_App/urls.py

from django.urls import path
from .views import PartnerPreferenceDetailsView

urlpatterns = [
    path('Partner_Preferences/', PartnerPreferenceDetailsView.as_view(), name='partner_preferences_api'),
]
