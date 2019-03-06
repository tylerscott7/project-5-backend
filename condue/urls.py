from django.contrib import admin
from django.urls import path, include
from .views import login, sample_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/login', login),
    path('api/users/sampleapi', sample_api),
    path('', include('reservation.urls')),
    path('', include('review.urls')),
    path('', include('user.urls')),
]
