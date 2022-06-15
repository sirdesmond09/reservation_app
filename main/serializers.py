from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    prev_reservation = serializers.ReadOnlyField()
    
    class Meta:
        model = Reservation
        fields = '__all__'