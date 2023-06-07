from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from shared.mixins import CustomIdModelMixin
from .resource import Resource

User = get_user_model()


class ResourceBorrow(CustomIdModelMixin):
    class Meta:
        verbose_name = _("resource borrow")
        verbose_name_plural = _("resource borrows")

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    resource = models.ForeignKey(to=Resource, on_delete=models.CASCADE)
    issue_timestamp = models.DateTimeField(_("issue timestamp"), default=timezone.now)
    due_timestamp = models.DateTimeField(_("due timestamp"), null=True)
    is_returned = models.BooleanField(_("is returned"), default=False)

    def __str__(self) -> str:
        return f"{self.user} -> {self.resource}"
