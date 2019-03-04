from rest_framework import serializers
from review.models import Review

# Reservation Serializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'