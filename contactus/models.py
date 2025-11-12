from django.db import models

class ContactUs(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    service = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name or ''} {self.last_name or ''} - {self.email or ''}"
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ['-created_at']


class ZohoLeadLog(models.Model):
    contact = models.ForeignKey(ContactUs, on_delete=models.CASCADE, related_name="zoho_logs")
    status = models.CharField(max_length=50)  # e.g., SUCCESS / ERROR
    response_code = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.status} - {self.contact.email or 'Unknown'}"

    class Meta:
        verbose_name = "Zoho Lead Log"
        verbose_name_plural = "Zoho Lead Logs"
        ordering = ['-created_at']
