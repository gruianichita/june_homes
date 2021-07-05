from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from june_homes.apps.hotels.models import Hotel


@api_view(['POST'])
def like_hotel_view(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    with transaction.atomic():
        hotel.likes += 1
        hotel.save()
        return HttpResponse({'details': 'success'})


@api_view(['POST'])
def dislike_hotel_view(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)

    with transaction.atomic():
        hotel.dislikes += 1
        hotel.save()
        return HttpResponse({'details': 'success'})
