from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from reservations_backend.apps.brand.models import Brand


class EventType(models.TextChoices):
    Tasting = 1, _("Tasting")
    Visit = 2, _("Visit")
    SpecialEvent = 3, _("Special Event")


class Event(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=100, blank=False, null=False)

    event_type = models.IntegerField(
        choices=EventType.choices,
        default=EventType.Visit,
    )

    date_started = models.DateTimeField(blank=False, null=False)
    date_ended = models.DateTimeField(blank=True, null=True)

    date_updated = models.DateTimeField(auto_now=True, null=False)
    date_created = models.DateTimeField(auto_now=True, null=False)
    date_deleted = models.DateTimeField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=False, null=False)
