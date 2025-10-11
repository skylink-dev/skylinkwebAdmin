from django.urls import path
from .views import ContactUsListCreateAPI, ContactUsDetailAPI

urlpatterns = [
    path('contacts/', ContactUsListCreateAPI.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactUsDetailAPI.as_view(), name='contact-detail'),
]
