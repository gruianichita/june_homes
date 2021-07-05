from rest_framework import serializers

from june_homes.apps.rooms.models import Room


class RoomSoldOutSerializer(serializers.ModelSerializer):
    sold_out = serializers.BooleanField()

    class Meta:
        model = Room
        fields = 'id', 'title', 'sold_out'
