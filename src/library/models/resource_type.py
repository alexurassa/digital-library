from django.db import models
from django.utils.translation import gettext_lazy as _


class ResourceType(models.Model):
    """Specifies the kind of resource. Example: Book, Magazine"""

    name = models.CharField(_("type name"), max_length=60)

    def __str__(self) -> str:
        return self.name
