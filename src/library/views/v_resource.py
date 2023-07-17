from django.views import View, generic
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

from shared.utils import get_instance_or_404
from ..models import Resource
from ..forms import ResourceForm


@method_decorator(permission_required("add_resource", settings.LOGIN_URL), name="post")
class ResourcesListCreateView(generic.ListView, generic.CreateView):
    """Ability to see available resources and add resource"""

    template_name = "library/resources/resource_list.html"
    form_class = ResourceForm

    def get(self, request, *args, **kwargs):
        context = {"resources": self.get_queryset(), "resource_form": self.form_class}
        return render(request, self.template_name, context)

    def get_queryset(self):
        return Resource.objects.all()

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Resource: {form.instance.title} added successfully"
            )
            return redirect("library:resources")
        else:
            self.form_class = form
            messages.error(request, "Form is filled incorrectly")
            return redirect("library:resources")


@method_decorator(permission_required("library.change_resource"), name="post")
class ResourceDetailUpdateView(generic.DetailView, generic.UpdateView):
    template_name = "library/resources/resource-detail.html"
    form_class = ResourceForm

    def get_object(self):
        return get_instance_or_404(view=self, model=Resource)

    def get(self, request, **kwargs):
        return render(
            request,
            self.template_name,
            {
                "form": self.form_class(data=vars(self.get_object())),
                "resource": self.get_object(),
            },
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.has_changed() and form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        instance = Resource.objects.filter(pk=self.get_object().pk)
        instance.update(
            publisher=cleaned_data.get("publisher"),
            category=cleaned_data.get("category"),
            type=cleaned_data.get("type"),
            title=cleaned_data.get("title"),
            description=cleaned_data.get("description"),
            frontCover=cleaned_data.get("frontCover"),
        )
        messages.success(self.request, "Resource updated successfully")
        return redirect(self.get_success_url())

    def get_success_url(self) -> str:
        return f"/library/resources/{self.get_object().pk}/detail"


@method_decorator(permission_required("library.delete_resource"), name="dispatch")
class ResourceDeleteView(generic.DeleteView):
    template_name = "library/resources/delete-resource.html"

    def get_object(self):
        return get_instance_or_404(view=self, model=Resource)

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        messages.success(request, "Resource deleted successfully")
        return redirect(self.get_success_url())

    def get_success_url(self) -> str:
        return "/library/resources"
