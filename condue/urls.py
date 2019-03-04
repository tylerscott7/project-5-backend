from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('reservation.urls')),
    path('', include('review.urls')),
]
