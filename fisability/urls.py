from django.urls import path
from .views import (
    CoverageAreaListCreateView,
    CoverageAreaDetailView,
    check_availability
)
from django.contrib.admin.views.decorators import staff_member_required
from .views import admin_map_view
urlpatterns = [
    path("coverage/", CoverageAreaListCreateView.as_view(), name="coverage-list"),
    path("coverage/<int:pk>/", CoverageAreaDetailView.as_view(), name="coverage-detail"),

    
    path("check/", check_availability, name="check-availability"),
     path("map/", staff_member_required(admin_map_view), name="coverage-map"),
]
