from rest_framework import generics
from .models import ContactUs, ZohoLeadLog
from .serializers import ContactUsSerializer
from django.views.decorators.csrf import csrf_exempt
import requests
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class ContactUsListCreateAPI(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all().order_by('-created_at')
    serializer_class = ContactUsSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

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
            response.raise_for_status()
            ZohoLeadLog.objects.create(
                contact=contact,
                status="SUCCESS",
                response_code=response.status_code,
                message="Lead pushed to Zoho successfully."
            )
        except requests.exceptions.RequestException as e:
            ZohoLeadLog.objects.create(
                contact=contact,
                status="ERROR",
                message=str(e)
            )

        return contact

@method_decorator(csrf_exempt, name='dispatch')
class ContactUsDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
