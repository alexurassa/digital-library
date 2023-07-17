from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from shared.mixins import CustomIdModelMixin
from .resource_category import ResourceCategory
from .author import Author
from .resource_type import ResourceType


class Resource(CustomIdModelMixin):
    """Specify any learning resource found in library"""

    class Meta:
        verbose_name = _("resource")
        verbose_name_plural = _("resources")
        ordering = ["title", "-registered_timestamp"]

    title = models.CharField(_("title"), max_length=100)
    published_date = models.DateField(_("published date"), default=timezone.now)
    publisher = models.CharField(_("publisher"), max_length=250)
    authors = models.ManyToManyField(Author, through="ResourceAuthor")
    frontCover = models.ImageField(
        _("front cover"),
        max_length=255,
        upload_to="library/resources/covers/",
        default="library/resources/covers/default.jpg",
    )
    registered_timestamp = models.DateTimeField(
        _("registered timestamp"), auto_now_add=True
    )
    category = models.ForeignKey(
        to=ResourceCategory, on_delete=models.SET_NULL, null=True
    )
    description = models.TextField(
        _("description"), null=True, blank=True, max_length=999
    )
    type = models.ForeignKey(to=ResourceType, on_delete=models.SET_NULL, null=True)
    is_borrowed = models.BooleanField(_("borrowed?"), default=False)

    def __str__(self) -> str:
        return self.title


class ResourceAuthor(models.Model):
    """The intermediate table between `Resource` and `Author`"""

    class Meta:
        verbose_name = _("resource author")
        verbose_name_plural = _("resource authors")

    resource = models.ForeignKey(
        to=Resource, on_delete=models.CASCADE, verbose_name=_("resource")
    )
    author = models.ForeignKey(
        to=Author, on_delete=models.CASCADE, verbose_name=_("author")
    )
    authored_date = models.DateField(_("date of authorship"), null=True)

    def __str__(self) -> str:
        return f"{self.author} -> {self.resource}"
