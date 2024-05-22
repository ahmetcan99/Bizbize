from django.db.models.signals import post_save
from users.models import CustomUser as User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def CreateProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def SaveProfile(sender, instance, **kwargs):
    instance.profile.save()