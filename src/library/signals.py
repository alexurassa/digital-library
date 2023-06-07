from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import *
from .utils import generateInstanceId


@receiver(signal=pre_save, sender=Resource)
def generateResourceId(sender, instance, **kwargs):
    return generateInstanceId(instance, length=20, is_upper=True, has_dashes=True)


@receiver(signal=pre_save, sender=Author)
def generateAuthorId(sender, instance, **kwargs):
    return generateInstanceId(instance, length=20)


@receiver(signal=pre_save, sender=ResourceBorrow)
def generateBorrowId(sender, instance, **kwargs):
    return generateInstanceId(instance, length=20)
