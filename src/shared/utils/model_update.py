from django.db.models import Model
from django.forms import ModelForm
from django.views.generic import DetailView, UpdateView


def perform_update(view: DetailView or UpdateView, model, form: ModelForm) -> None:
    """Update an instance found in `get_object()` method of the `DetailView` or `UpdateView` or base class `View`"""

    instance, _ = model.objects.update_or_create(
        pk=view.get_object().pk, defaults=form.cleaned_data
    )
