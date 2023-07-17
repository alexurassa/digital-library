from django.views import generic, View
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shared.utils import get_instance_or_404
from ..models import Resource, ResourceBorrow


class ResourcesChecklistView(View):
    template_name = "library/resources/checklist.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"checklist": self.get_queryset()})

    def get_queryset(self):
        return Resource.objects.filter(is_borrowed=False)


@method_decorator(login_required(login_url=settings.LOGIN_URL), name="post")
class ChecklistItemDetailView(generic.DetailView, generic.CreateView):
    template_name = "library/resources/checklist-detail.html"

    def get_object(self):
        return get_instance_or_404(view=self, model=Resource)

    def get(self, request, **kwargs):
        return render(request, self.template_name, {"resource": self.get_object()})

    def post(self, request, *args, **kwargs):
        resource = self.get_object()
        if not resource.is_borrowed:
            borrow = ResourceBorrow.objects.create(
                user=self.request.user, resource=resource
            )
            borrow.save()
            messages.success(request, f"Your borrow request has been created")
            return redirect(self.get_success_url())
        else:
            messages.error(request, "The resource your requesting is borrowed")
            return redirect(self.get_success_url())

    def get_success_url(self):
        return "/library/resources/checklist"
