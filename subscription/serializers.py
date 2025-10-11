from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import EmailSubscription

class SubscribeAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'status': 'error', 'message': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            return Response({'status': 'error', 'message': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if email already exists
        subscription, created = EmailSubscription.objects.get_or_create(email=email)

        if created:
            return Response({'status': 'success', 'message': 'Subscribed successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'success', 'message': 'Email already subscribed'}, status=status.HTTP_200_OK)
