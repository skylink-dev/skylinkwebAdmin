from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from math import radians, sin, cos, sqrt, atan2
import json
from .models import CoverageArea
from rest_framework import generics
from .serializers import CoverageAreaSerializer
from django.shortcuts import render, get_object_or_404
from django.conf import settings
import requests
from urllib.parse import quote


# ----------------------------------------------------------
# Utility: Distance Calculation (Haversine Formula)
# ----------------------------------------------------------
def distance_km(lat1, lng1, lat2, lng2):
    R = 6371.0  # Earth radius in km

    dlat = radians(lat2 - lat1)
    dlng = radians(lng2 - lng1)

    a = (sin(dlat / 2) ** 2 +
         cos(radians(lat1)) * cos(radians(lat2)) *
         sin(dlng / 2) ** 2)

    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


# ----------------------------------------------------------
# API: Coverage Availability
# ----------------------------------------------------------
@csrf_exempt
def check_availability(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        data = json.loads(request.body)
        lat = data.get("lat")
        lng = data.get("lng")
        address = data.get("address")
    except:
        return JsonResponse({"error": "Invalid payload"}, status=400)

    # If lat/lng provided, skip geocoding
    if lat and lng:
        pass
    elif address:
        geo = geocode_address(address)
        if not geo:
            return JsonResponse({"error": "Unable to find location for this address"}, status=400)
        lat, lng = geo
    else:
        return JsonResponse({"error": "Address or lat/lng required"}, status=400)

    # Check coverage
    for area in CoverageArea.objects.all():
        dist = distance_km(float(lat), float(lng), area.center_lat, area.center_lng)

        if dist <= area.radius_km:
            return JsonResponse({
                "available": True,
                "input_address": address if address else None,
                "lat": lat,
                "lng": lng,
                "city": area.city,
                "area_name": area.area_name,
                "distance_km": round(dist, 3),
                "radius_km": area.radius_km
            })

    return JsonResponse({
        "available": False,
        "input_address": address if address else None,
        "lat": lat,
        "lng": lng
    })


# ----------------------------------------------------------
# Admin Map Views
# ----------------------------------------------------------
def admin_map_view(request):
    area_id = request.GET.get("id")
    area = get_object_or_404(CoverageArea, id=area_id)

    return render(request, "admin/map_view.html", {
        "area": area,
        "google_api_key": settings.GOOGLE_API_KEY,
    })


def admin_all_map_view(request):
    areas = CoverageArea.objects.all()

    return render(request, "admin/map_all.html", {
        "areas": areas,
        "google_api_key": settings.GOOGLE_API_KEY,
    })


# ----------------------------------------------------------
# Geocoding Utility
# ----------------------------------------------------------
def geocode_address(address):
    encoded = quote(address)
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={encoded}&key={settings.GOOGLE_API_KEY}"

    response = requests.get(url).json()

    if response.get("status") != "OK":
        print("Geocode Error:", response)  # Debug logging
        return None

    location = response["results"][0]["geometry"]["location"]
    return location["lat"], location["lng"]


# ----------------------------------------------------------
# CRUD APIs for CoverageArea (DRF)
# ----------------------------------------------------------
class CoverageAreaListCreateView(generics.ListCreateAPIView):
    queryset = CoverageArea.objects.all()
    serializer_class = CoverageAreaSerializer


class CoverageAreaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoverageArea.objects.all()
    serializer_class = CoverageAreaSerializer