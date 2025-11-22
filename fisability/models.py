from django.db import models

class CoverageArea(models.Model):
    city = models.CharField(max_length=100, default="Unknown")
    area_name = models.CharField(max_length=100, default="Unnamed Area")
    center_lat = models.FloatField(default=0.0)
    center_lng = models.FloatField(default=0.0)
    radius_km = models.FloatField(default=1.0)  # You can increase the default radius

    def __str__(self):
        return f"{self.city} - {self.area_name}"
