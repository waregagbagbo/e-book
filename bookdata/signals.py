from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from .models import Profile



@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# Create a Profile for each new user.
#post_save.connect(create_profile, sender=User)
        

'''@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()'''
   