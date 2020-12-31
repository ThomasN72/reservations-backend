from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from reservations_backend.apps.reservation import serializers
from reservations_backend.apps.reservation.models import Reservation


class ReservationView(APIView):
    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = serializers.ReservationSerializer(reservations, many=True, partial=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.PostReservationSerializer(data=request.data, partial=True)
        if serializer.is_valid() == False:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(status=status.HTTP_200_OK)
