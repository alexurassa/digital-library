from django import forms
from ..models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ("id",)

    def update(self, instance, cleaned_data):
        instance.full_name = cleaned_data.get("full_name", instance.full_name)
        instance.email = cleaned_data.get("email", instance.email)
        instance.address = cleaned_data.get("address", instance.address)
        instance.save()
        return instance
