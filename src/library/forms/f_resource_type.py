from django import forms
from ..models import ResourceType


class ResourceTypeForm(forms.ModelForm):
    class Meta:
        model = ResourceType
        fields = [
            "name",
        ]
