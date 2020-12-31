from uuid import uuid4

from django.db import models

from reservations_backend.apps.event.models import Event
# Create your models here.
from reservations_backend.apps.profile.models import Profile


class Reservation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4)
    date_updated = models.DateTimeField(auto_now=True, null=False)
    date_created = models.DateTimeField(auto_now=True, null=False)
    date_deleted = models.DateTimeField(blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
