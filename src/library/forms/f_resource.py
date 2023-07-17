from django import forms
from ..models import Resource, ResourceCategory, ResourceType


class ResourceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ResourceForm, self).__init__(*args, **kwargs)
        self.fields["category"].queryset = ResourceCategory.objects.all()
        self.fields["type"].queryset = ResourceType.objects.all()
        self.fields["published_date"].widget = forms.DateInput(attrs={"type": "date"})

    class Meta:
        model = Resource
        exclude = ["authors", "id"]
