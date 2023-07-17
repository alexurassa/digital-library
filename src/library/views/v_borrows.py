from django.views import generic, View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib import messages
from django.conf import settings
from shared.utils import get_instance_or_404
from ..models import ResourceBorrow
from ..forms import BorrowForm


@method_decorator(
    user_passes_test(
        lambda user: user.is_superuser or user.is_staff, settings.LOGIN_URL
    ),
    name="dispatch",
)
class BorrowedResourcesListView(generic.ListView):
    """Only can be used by `superusers` and `staff` users"""

    template_name = "library/resources/borrowed-resources.html"

    def get(self, request, *args, **kwargs):
        return render(
            request, self.template_name, {"borrowed_resources": self.get_queryset()}
        )

    def get_queryset(self):
        return ResourceBorrow.objects.all()


class BorrowedResourceDetailUpdateView(generic.DetailView, generic.UpdateView):
    template_name = "library/resources/borrowed-resource-detail.html"
    form_class = BorrowForm

    def get_object(self):
        return get_instance_or_404(view=self, model=ResourceBorrow)

    def get(self, request, **kwargs):
        form = self.form_class(data=vars(self.get_object()))
        return render(
            request,
            self.template_name,
            {"borrowed_resource": self.get_object(), "form": form},
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.has_changed() and form.is_valid():
            return self.form_valid(form)
        else:
            messages.error(request, "Form filled Incorrectly")
            return redirect(self.get_success_url())

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        borrow = ResourceBorrow.objects.filter(pk__exact=self.get_object().pk)
        borrow.update(
            issue_confirmed=cleaned_data.get("issue_confirmed"),
            is_returned=cleaned_data.get("is_returned"),
            due_timestamp=cleaned_data.get("due_timestamp"),
            resource=cleaned_data.get("resource"),
        )
        borrow.first().save()
        messages.success(self.request, "Updated successfully")
        return redirect(self.get_success_url())

    def get_success_url(self):
        return f"/library/borrows/{self.get_object().pk}/detail/"


@method_decorator(permission_required("library.delete_resourceborrow"), name="dispatch")
class DeleteBorrowedResourceView(generic.DeleteView):
    template_name = "library/resources/delete-borrowed-resource.html"

    def get_object(self):
        return get_instance_or_404(view=self, model=ResourceBorrow)

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        messages.success(request, "Borrowed Item deleted successfully")
        return redirect(self.get_success_url())

    def get_success_url(self) -> str:
        return "/library/borrows/"

    def get_queryset(self):
        return ResourceBorrow.objects.all()
