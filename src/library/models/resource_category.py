from django.db import models
from django.utils.translation import gettext_lazy as _


class ResourceCategory(models.Model):
    """A category that informs resources that are related"""

    class Meta:
        verbose_name = _("resource category")
        verbose_name_plural = _("resource categories")

    name = models.CharField(_("name"), max_length=150)

    def __str__(self) -> str:
        return self.name
