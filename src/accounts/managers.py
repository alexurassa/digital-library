from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Custom model manager for `AUTH_USER_MODEL`"""

    def create_user(
        self, email: str, first_name: str, last_name: str, password: str, **extra_fields
    ):
        if not email:
            raise ValueError(_("Email is required"))
        if not first_name:
            raise ValueError(_("First name is required"))
        if not last_name:
            raise ValueError(_("First name is required"))

        normalized_email = self.normalize_email(email)

        # set defaults
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        # create user
        created_user = self.model(
            email=normalized_email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        created_user.set_password(password)

        created_user.save(using=self._db)

        return created_user

    def create_staffuser(
        self, email: str, first_name: str, last_name: str, password: str, **extra_fields
    ):
        """Must have staff status set to `True`"""

        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)

        return self.create_user(email, first_name, last_name, password, **extra_fields)

    def create_superuser(
        self, email: str, first_name: str, last_name: str, password: str, **extra_fields
    ):
        """Admins should have superuser status set to True"""

        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, first_name, last_name, password, **extra_fields)
