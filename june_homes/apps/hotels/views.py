import datetime

from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from june_homes.apps.hotels.models import Hotel
from june_homes.apps.hotels.serializers import HotelSerializer


@api_view(['POST'])
def like_hotel_view(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    with transaction.atomic():
        hotel.likes += 1
        hotel.save()
        return Response({'details': 'success'})


@api_view(['POST'])
def dislike_hotel_view(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    with transaction.atomic():
        hotel.dislikes += 1
        hotel.save()
        return Response({'details': 'success'})


class HotelsWithFreeRoomsView(APIView):

    def get(self, request):
        today = timezone.now().date()

        hotels = Hotel.objects.filter(
            Q(rooms__reservations__start__gt=today)
            |
            Q(rooms__reservations__end__lt=today)
        )
        return Response(HotelSerializer(hotels, many=True).data)
