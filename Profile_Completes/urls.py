# Profile_Completes/urls.py

from django.urls import path
from .views import ProfileCompletesView

urlpatterns = [
    path('profile_completes/', ProfileCompletesView.as_view(), name='profile_completes_api'),
]
