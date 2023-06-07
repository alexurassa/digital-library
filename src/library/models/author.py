from django.db import models
from django.utils.translation import gettext_lazy as _


from shared.mixins import CustomIdModelMixin


class Author(CustomIdModelMixin):
    """Specifies the writer of the `LearningResource`"""

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")

    full_name = models.CharField(_("full name"), max_length=100)
    email = models.EmailField(_("email"), max_length=255, null=True)
    address = models.CharField(_("address"), max_length=245, null=True)

    def __str__(self) -> str:
        return self.full_name
