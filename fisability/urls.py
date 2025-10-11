from django.urls import path
from .views import CheckAvailabilityAPI

urlpatterns = [
    path('check-availability/', CheckAvailabilityAPI.as_view(), name='check-availability'),
]
