from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

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


@receiver(signal=pre_save, sender=ResourceBorrow)
def generateBorrowDateOfIssue(sender, instance, **kwargs):
    if instance.issue_timestamp is None and instance.issue_confirmed:
        instance.issue_timestamp = timezone.now()


@receiver(signal=post_save, sender=ResourceBorrow)
def changeBorrowStatus(created, sender, instance, **kwargs):
    if not instance.is_returned:
        instance.resource.is_borrowed = True
    else:
        instance.resource.is_borrowed = False
