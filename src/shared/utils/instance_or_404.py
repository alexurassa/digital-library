from django.shortcuts import get_object_or_404
from django.db.models import Model


def get_instance_or_404(view, model: Model, lookup_kwarg: str = "pk"):
    return get_object_or_404(model, id__exact=view.kwargs.get(lookup_kwarg))
