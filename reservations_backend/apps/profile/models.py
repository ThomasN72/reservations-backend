from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Extend Djano User Model
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.CharField(max_length=500, blank=True, null=False, default="")
    address = models.CharField(max_length=256, blank=True, null=False, default="")
    city = models.CharField(max_length=50, blank=True, null=False, default="")
    postal_code = models.CharField(max_length=10, blank=True, null=False, default="")
    birth_date = models.DateField(null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=False)
    date_created = models.DateTimeField(auto_now=True, null=False)
    date_deleted = models.DateTimeField(blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
