from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

#
class User(AbstractUser):
    is_individual = models.BooleanField(default=False)
    is_master = models.BooleanField(default=False)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
         Token.objects.create(user=instance) 


class Individual(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE, related_name='individual')

    def __str__(self):
        return self.user.username


class Master(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='master')

    def __str__(self):
        return self.user.username