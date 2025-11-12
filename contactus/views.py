from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ContactUs
from .serializers import ContactUsSerializer
import requests  # for sending data to Zoho

class ContactUsListCreateAPI(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all().order_by('-created_at')
    serializer_class = ContactUsSerializer

    def perform_create(self, serializer):
        contact = serializer.save()  # Save to local DB first

        # --- Send data to Zoho CRM Web-to-Lead ---
        zoho_url = "https://crm.zoho.in/crm/WebToLeadForm"
        payload = {
            "xnQsjsdp": "4baf747f51b50041d5f3fcb34d8658593970bb7f969c23e4e378318ac6e0813d",
            "xmIwtLD": "fc428e61ab0d3a796fd04d88fd0d5b901dccda909a669687990e5b9571cc6b476e36acfe1b4152b6eef506853f4f2a65",
            "actionType": "TGVhZHM=",
            "returnURL": "http://stage.skylink.net.in:3000/",
            "Last Name": contact.last_name or contact.first_name or "No Name",
            "Email": contact.email or "",
            "Mobile": contact.phone or "",
            "Lead Source": "Website",
        }

        try:
            response = requests.post(zoho_url, data=payload)
            response.raise_for_status()  # raise error if failed
        except requests.exceptions.RequestException as e:
            print("⚠️ Zoho CRM POST failed:", e)

        return contact  # optional, already handled by DRF


class ContactUsDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
