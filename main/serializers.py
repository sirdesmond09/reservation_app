from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    prev_reservation = serializers.ReadOnlyField()
    rental_name = serializers.ReadOnlyField()
    class Meta:
        model = Reservation
        fields = ["rental_name","res_id","checkin","checkout","prev_reservation","rental"]
        extra_kwargs = {
            'rental': {'write_only': True},
        }