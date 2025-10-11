from django.db import models

class Fisability(models.Model):
    circlename = models.CharField(max_length=100, blank=True, null=True, default='')
    regionname = models.CharField(max_length=100, blank=True, null=True, default='')
    divisionname = models.CharField(max_length=100, blank=True, null=True, default='')
    officename = models.CharField(max_length=100, blank=True, null=True, default='')
    pincode = models.CharField(max_length=10, blank=True, null=True, default='')
    officetype = models.CharField(max_length=50, blank=True, null=True, default='')
    delivery = models.CharField(max_length=50, blank=True, null=True, default='')
    district = models.CharField(max_length=100, blank=True, null=True, default='')
    statename = models.CharField(max_length=100, blank=True, null=True, default='')
    latitude = models.CharField(max_length=50, blank=True, null=True, default='')
    longitude = models.CharField(max_length=50, blank=True, null=True, default='')
    availability = models.BooleanField(default=False)  # user-updated availability

    def __str__(self):
        return f"{self.officename or ''} - {self.pincode or ''}"
