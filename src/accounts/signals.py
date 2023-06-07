from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from shared.utils import UUIDGenerator

User = get_user_model()


@receiver(pre_save, sender=User)
def generateUserId(sender, instance, **kwargs):
    if instance.id is None or instance.id == "":
        instance.id = UUIDGenerator.generate_string_token(length=20)
        instance.save()
