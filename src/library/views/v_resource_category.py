from django import forms
from django.views import generic
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

from ..models import ResourceCategory
from ..forms import ResourceCategoryForm
from shared.utils import get_instance_or_404


class ResourceCategoriesListCreateView(generic.ListView, generic.CreateView):
    """Ability to see library resource categories and create them"""

    form_class = ResourceCategoryForm
    template_name = "library/categories/resource-category-list.html"

    def get(self, request, *args, **kwargs):
        context = {
            "categories": self.get_queryset(),
            "category_form": self.form_class(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category saved successfully")
            return redirect("library:resource_categories")
        else:
            self.form_class = form
            messages.error(request, "Form contain errors")
            return redirect("library:resource_categories")

    def get_queryset(self):
        return ResourceCategory.objects.all()


@method_decorator(permission_required("library.change_resourcecategory"), name="post")
class CategoryDetailUpdateView(View):
    template_name = "library/categories/resource-category-detail.html"
    form_class = ResourceCategoryForm

    def get_object(self):
        return get_instance_or_404(view=self, model=ResourceCategory, lookup_kwarg="id")

    def get(self, request, *args, **kwargs):
        context = {
            "category": self.get_object(),
            "form": self.form_class(data=vars(self.get_object())),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.has_changed() and form.is_valid():
            return self.form_valid(form)
        else:
            self.form_class = form
            messages.error(request, "Form is not valid")
            return redirect("library:resource_category_detail", self.get_object().id)

    def form_valid(self, form: forms.Form):
        category, _ = ResourceCategory.objects.update_or_create(
            pk=self.get_object().pk, defaults=form.cleaned_data
        )
        messages.success(self.request, "Category updated successfully")
        return redirect("library:resource_categories")


@method_decorator(
    permission_required("library.delete_resourcecategory"), name="dispatch"
)
class ResourceCategoryDeleteView(generic.DeleteView):
    template_name = "library/categories/category-delete.html"

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        messages.success(request, "Category deleted successfully")
        return redirect(self.get_success_url())

    def get_success_url(self) -> str:
        return "/library/resource-categories/"

    def get_queryset(self):
        return ResourceCategory.objects.all()
