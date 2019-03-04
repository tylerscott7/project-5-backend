from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    numGuests = models.SmallIntegerField()
    note = models.CharField(max_length=100)