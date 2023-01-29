from django.dispatch import receiver
from .models import User, Profile
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_profile_post_save(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)