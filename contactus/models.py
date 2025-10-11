from django.db import models

class ContactUs(models.Model):
    first_name = models.CharField(max_length=50, default='', blank=True, null=True)
    last_name = models.CharField(max_length=50, default='', blank=True, null=True)
    phone = models.CharField(max_length=15, default='', blank=True, null=True)
    email = models.EmailField(default='', blank=True, null=True)
    message = models.TextField(default='', blank=True, null=True)
    service = models.CharField(max_length=100, default='', blank=True, null=True)
    address = models.CharField(max_length=255, default='', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)  # date & time when created
    updated_at = models.DateTimeField(auto_now=True)      # date & time when updated

    def __str__(self):
        return f"{self.first_name or ''} {self.last_name or ''} - {self.email or ''}"
