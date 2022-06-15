import aifc
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from main.serializers import ReservationSerializer
from .models import Reservation

@api_view(["GET"])
def get_reservations(request):
    if request.method == 'GET':
        data = Reservation.objects.all()
        serializer = ReservationSerializer(data, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    