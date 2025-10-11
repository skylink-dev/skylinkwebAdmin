from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Fisability

class CheckAvailabilityAPI(APIView):
    def post(self, request):
        data = request.data
        if not isinstance(data, dict):
            return Response({'error': 'Invalid data format, JSON expected'}, status=status.HTTP_400_BAD_REQUEST)

        pincode = data.get('pincode')
        if not pincode:
            return Response({'error': 'Pincode is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if any entry exists with this pincode
        exists = Fisability.objects.filter(pincode=pincode).exists()
        availability = False
        if exists:
            # Get the availability of the first record with this pincode
            availability = Fisability.objects.filter(pincode=pincode).first().availability

        return Response({
            'pincode': pincode,
            'exists': exists,
            'availability': availability
        }, status=status.HTTP_200_OK)
