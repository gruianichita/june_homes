from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from june_homes.apps.users.serializers import UserSerializer


class LivingMarylandView(APIView):

    def get(self, request):
        users = User.objects.filter(reservations__room__hotel__title='Maryland').distinct()
        return Response(UserSerializer(users, many=True).data)
