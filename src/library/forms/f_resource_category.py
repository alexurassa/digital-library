from django import forms
from ..models import ResourceCategory


class ResourceCategoryForm(forms.ModelForm):
    class Meta:
        model = ResourceCategory
        fields = "__all__"
