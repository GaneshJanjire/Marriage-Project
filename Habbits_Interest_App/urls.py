# Habbits_Interest_App/urls.py

from django.urls import path
from .views import HabbitsInterestView

urlpatterns = [
    path('Hobbits_Interest/', HabbitsInterestView.as_view(), name='habbits_interest_api'),
]
