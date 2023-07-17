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
    issue_timestamp = models.DateTimeField(_("issue timestamp"), null=True)
    due_timestamp = models.DateTimeField(_("due timestamp"), null=True)
    issue_confirmed = models.BooleanField(_("confirm issue"), default=False)
    is_returned = models.BooleanField(_("is returned"), default=False)

    def __str__(self) -> str:
        return f"{self.user} -> {self.resource}"

    # def save(self, *args, **kwargs):
    #     if self.is_returned:
    #         self.resource.is_borrowed = False
    #         print("is returned executed")
    #     else:
    #         print("is not returned not executed")
    #         self.resource.is_borrowed = True
    #     self.resource.save(*args, **kwargs)
    #     print("resource borrowed", self.resource.is_borrowed)
    #     return super().save(*args, **kwargs)
