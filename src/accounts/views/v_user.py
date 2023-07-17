from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

# from django.contrib.auth import get_user_model
from ..models import User
from ..forms import UserForm


@method_decorator(
    user_passes_test(lambda user: user.is_staff or user.is_superuser), name="dispatch"
)
class LibraryUsersListCreateView(generic.ListView, generic.CreateView):
    template_name = "accounts/users/users-list-create.html"
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {"users": self.get_queryset(), "form": self.form_class(label_suffix="")},
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        return redirect("accounts:users")

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, f"User: {form.instance.first_name} is added successfully"
        )
        return redirect("accounts:users")

    def get_queryset(self):
        return User.objects.values(
            "first_name", "last_name", "email", "is_active", "is_staff", "is_superuser"
        )
