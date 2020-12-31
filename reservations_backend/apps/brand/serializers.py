from rest_framework import serializers

from reservations_backend.apps.brand.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        # fields = ['id', 'name', 'event_type', 'date_started', 'date_ended', 'brand']
