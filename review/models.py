from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100)
    stars = models.SmallIntegerField()
    note = models.CharField(max_length=100)