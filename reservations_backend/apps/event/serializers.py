from rest_framework import serializers

from reservations_backend.apps.brand.serializers import BrandSerializer
from reservations_backend.apps.event.models import Event


class EventSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Event
        fields = '__all__'
        # fields = ['id', 'name', 'event_type', 'date_started', 'date_ended', 'brand']
