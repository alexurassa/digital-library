from django import forms
from django.contrib.auth import get_user_model


class RegisterUserForm(forms.ModelForm):
    """Form to create a `user`"""

    password = forms.CharField(
        max_length=128,
        min_length=8,
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        max_length=128,
        min_length=8,
        label="Confirm password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "password",
            "password2",
        ]

    def clean(self):
        return super().clean()

    def clean_email(self):
        "Reject if user with `email` already exists"

        email = self.cleaned_data["email"]
        if email and self._meta.model.objects.filter(email__exact=email).exists():
            raise forms.ValidationError(
                f"User with email <{email}> already exists", code="unique"
            )
        else:
            return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.errors["password_mismatch"], code="password_mismatch"
            )

        return password2
