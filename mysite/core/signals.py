from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Enable Profile instance to be created once a user instance is creted, 

@receiver(post_save, sender=User)
def create_profile(sender, instance , created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveprofile(sender, instance , **kwargs):
    instance.profile.save()


# ...more code on apps.py        


