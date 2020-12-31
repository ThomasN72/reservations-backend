from uuid import uuid4

from django.db import models

# Create your models here.


class Brand(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=100, blank=False, null=False)
    logo = models.CharField(max_length=500, blank=True, null=False, default="")
    description = models.TextField(blank=True, null=False, default="")
    address = models.CharField(max_length=256, blank=True, null=False, default="")
    city = models.CharField(max_length=50, blank=True, null=False, default="")
    postal_code = models.CharField(max_length=10, blank=True, null=False, default="")
    date_updated = models.DateTimeField(auto_now=True, null=False)
    date_created = models.DateTimeField(auto_now=True, null=False)
    date_deleted = models.DateTimeField(blank=True, null=True)
