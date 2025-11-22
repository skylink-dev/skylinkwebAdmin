from django.urls import path
from .views import trigger_3cx_call

urlpatterns = [
    path("makecall/", trigger_3cx_call, name="trigger_3cx_call"),
]
