from django.db import models

class Places(models.Model):
    PlaceID = models.AutoField(primary_key=True)
    PhotoPlace = models.CharField(max_length=500)
    PlaceName = models.CharField(max_length=500)
    PlaceLocation = models.CharField(max_length=500)
    PlaceRate = models.FloatField(max_length= 10)
    PlacePrice = models.FloatField(max_length=10)
