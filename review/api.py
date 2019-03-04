from review.models import Review
from rest_framework import viewsets, permissions
from .serializers import ReviewSerializer

# Reservation Viewset
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReviewSerializer