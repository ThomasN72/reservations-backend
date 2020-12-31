from rest_framework import serializers

from reservations_backend.apps.profile.models import Profile
from reservations_backend.apps.user.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'
