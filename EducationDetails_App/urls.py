# EducationDetails_App/urls.py

from django.urls import path
from .views import EducationDetailsView

urlpatterns = [
    path('EducationDetails_App/', EducationDetailsView.as_view(), name='education_api'),
]
