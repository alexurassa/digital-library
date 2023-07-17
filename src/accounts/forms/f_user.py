from django import forms
from ..models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "password",
            "password2",
        ]

    password2 = forms.CharField(
        max_length=128,
        min_length=8,
        widget=forms.PasswordInput(attrs={"auto-complete": "new-password"}),
        label="Confirm password",
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("passwords")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

        return password2

    def clean_email(self):
        chosen_email = self.cleaned_data.get("email")
        if self._meta.model.objects.filter(email__exact=chosen_email).exists():
            raise forms.ValidationError(
                "User with email %s already exists" % chosen_email
            )
        return

    def save(self, commit=True):
        self._meta.model.objects.create_user(**self.cleaned_data)
