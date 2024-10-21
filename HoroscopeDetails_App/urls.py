# HoroscopeDetails_App/urls.py

from django.urls import path
from .views import HoroscopeDetailsView

urlpatterns = [
    path('horoscope/', HoroscopeDetailsView.as_view(), name='horoscope_api'),
]
