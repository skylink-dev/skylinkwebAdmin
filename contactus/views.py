from rest_framework import generics
from .models import ContactUs
from .serializers import ContactUsSerializer

# List all contacts or create a new one
class ContactUsListCreateAPI(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

# Retrieve, update, or delete a specific contact
class ContactUsDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
