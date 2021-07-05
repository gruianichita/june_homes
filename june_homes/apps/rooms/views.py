import datetime

from django.db.models import Case, When, BooleanField, Q
from rest_framework.response import Response
from rest_framework.views import APIView

from june_homes.apps.rooms.models import Room
from june_homes.apps.rooms.serializers import RoomSoldOutSerializer


class SoldOutView(APIView):

    def get_rooms_list_with_sold_out_sign(self, move_in, move_out):
        return Room.objects.filter(
            reservations__isnull=False
        ).annotate(sold_out=Case(
            When(
                ((
                         Q(reservations__start__gt=move_in)
                         & Q(reservations__start__lt=move_out)
                 )
                 |
                 (
                         Q(reservations__end__gt=move_in)
                         & Q(reservations__end__lt=move_out)
                 ))
                |
                Q(reservations__start=move_in)
                |
                Q(reservations__end=move_in)
                |
                Q(reservations__start=move_out)
                |
                Q(reservations__end=move_out)
                ,
                then=True
            ),
            default=False,
            output_field=BooleanField()
        ))

    def get(self, request):
        move_in = request.query_params.get('move_in')
        move_out = request.query_params.get('move_out')
        rooms = self.get_rooms_list_with_sold_out_sign(move_in, move_out)
        return Response(RoomSoldOutSerializer(rooms, many=True).data)
