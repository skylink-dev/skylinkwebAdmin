from django.urls import path
from .views import SubscribeAPI

urlpatterns = [
    path('subscribe/', SubscribeAPI.as_view(), name='subscribe'),
]
