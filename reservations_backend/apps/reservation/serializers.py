import os

from django.contrib.auth.models import User
from rest_framework import serializers

from reservations_backend.apps.event.serializers import EventSerializer
from reservations_backend.apps.profile.models import Profile
from reservations_backend.apps.profile.serializers import ProfileSerializer
from reservations_backend.apps.reservation.models import Reservation
from reservations_backend.apps.user.serializers import UserSerializer


class PostReservationSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    user = UserSerializer()

    class Meta:
        model = Reservation
        fields = '__all__'

    def create(self, validated_data):
        email = validated_data['user']['email']
        if email:
            profile = Profile.objects.filter(user__email=email).first()
            if profile is None:
                user = User(
                    username=email,
                    email=email,
                    password=os.environ["ANONYMOUSUSER_PASSWORD"])
                user.save()
        reservation = Reservation(profile=profile, event=validated_data["event"])
        reservation.save()

        return reservation


class ReservationSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    event = EventSerializer()

    class Meta:
        model = Reservation
        fields = '__all__'
