from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from bigsansar.contrib.account.models import userinfo


@receiver(post_save, sender=User)
def create_userinfo(sender, instance, created, **kwargs):
    if created:
        userinfo.objects.create(user=instance)
