from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomIdModelMixin(models.Model):
    """Mixin with a custom `id` field.

    You can overwrite the length of the instance `id` by specifying the `id_length`\n
    attribute in the top level of your child Model
    """

    id_length = 20

    class Meta:
        abstract = True

    id = models.CharField(_("id"), max_length=id_length, unique=True, primary_key=True)
