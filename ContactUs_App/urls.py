# ContactUs_App/urls.py

from django.urls import path
from .views import ContactView

urlpatterns = [
    path('ContactUs/', ContactView.as_view(), name='contact_api'),
]
