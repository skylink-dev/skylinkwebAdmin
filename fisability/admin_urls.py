from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from .views import admin_map_view, admin_all_map_view

urlpatterns = [
    path("map/", staff_member_required(admin_map_view), name="coverage-map"),
    path("all/", staff_member_required(admin_all_map_view), name="coverage-map-all"),
]
