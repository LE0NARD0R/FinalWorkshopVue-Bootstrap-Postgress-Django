from rest_framework import serializers
from carddeck.models import Places

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Places
        fields=('PlaceID', 'PhotoPlace', 'PlaceName', 'PlaceLocation','PlaceRate','PlacePrice')