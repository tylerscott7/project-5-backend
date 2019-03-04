from rest_framework import serializers
from reservation.models import Reservation

# Reservation Serializer
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'