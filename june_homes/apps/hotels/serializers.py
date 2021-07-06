from rest_framework import serializers

from june_homes.apps.hotels.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
