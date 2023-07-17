from typing import Any
from django.db import models
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.conf import settings
from shared.utils import get_instance_or_404

from ..models import ResourceType
from ..forms import ResourceTypeForm


@method_decorator(
    user_passes_test(
        lambda user: user.is_staff or user.is_superuser, settings.LOGIN_URL
    ),
    name="post",
)
@method_decorator(
    user_passes_test(lambda user: user.is_authenticated, settings.LOGIN_URL), name="get"
)
class ResourceTypesListCreateView(generic.ListView, generic.CreateView):
    template_name = "library/resource-types/types-list-create.html"
    form_class = ResourceTypeForm

    def get(self, request, **kwargs):
        return render(
            request,
            self.template_name,
            {"form": self.form_class(), "resource_types": self.get_queryset()},
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, f"A type: {form.instance.name} added successfully."
        )
        return redirect("library:resource_types")

    def get_queryset(self):
        return ResourceType.objects.all()


@method_decorator(permission_required("library.delete_resourcetype"), name="dispatch")
class ResourceTypeDeleteView(generic.DeleteView):
    template_name = "library/resource-types/delete-type.html"

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        messages.success(request, "Resource Type deleted successfully.")
        return redirect(self.get_success_url())

    def get_queryset(self):
        return ResourceType.objects.all()

    def get_success_url(self) -> str:
        return "/library/resource-types"


@method_decorator(permission_required("library.change_resourcetype"), name="post")
class ResourceTypeDetailUpdateView(generic.DetailView, generic.UpdateView):
    template_name = "library/resource-types/type-detail.html"
    form_class = ResourceTypeForm

    def get_object(self):
        return get_instance_or_404(view=self, model=ResourceType)

    def get(self, request, **kwargs):
        return render(
            request,
            self.template_name,
            {
                "form": self.form_class(data=vars(self.get_object())),
                "resource_type": self.get_object(),
            },
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            messages.error(request, "Please fill correctly")
            return redirect(self.get_success_url())

    def form_valid(self, form):
        type, _ = ResourceType.objects.update_or_create(
            pk=self.get_object().pk, defaults=form.cleaned_data
        )
        messages.success(self.request, "Type updated successfully")
        return redirect(self.get_success_url())

    def get_success_url(self) -> str:
        return f"/library/resource-types/{self.get_object().pk}/detail/"
