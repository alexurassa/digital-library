from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Representing users"""

    class Meta:
        ordering = ["date_joined", "first_name", "last_name"]
        verbose_name = _("user")
        verbose_name_plural = _("users")

    id = models.CharField(_("user ID"), max_length=20, unique=True, primary_key=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    middle_name = models.CharField(
        _("middle name"), max_length=150, null=True, blank=True
    )
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    email = models.EmailField(_("email address"), null=False, unique=True)
    password = models.CharField(_("password"), max_length=255, null=False)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    last_login = models.DateTimeField(_("last login"), default=timezone.now)
    is_active = models.BooleanField(_("active status"), default=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_superuser = models.BooleanField("superuser status", default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self) -> str:
        return f"<{self.first_name} {self.last_name}>"
