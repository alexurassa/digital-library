from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views import View

from ..forms import RegisterUserForm


User = get_user_model()


class RegisterUserView(View):
    """Use to create `User` accounts"""

    template_name = "auth/register.html"
    form_class = RegisterUserForm

    def get(self, request, *args, **kwargs):
        register_form = self.form_class
        return render(request, self.template_name, {"register_form": register_form})

    def post(self, request, *args, **kwargs):
        register_form = self.form_class(request.POST)
        if register_form.is_valid():
            user = User.objects.create(register_form.cleaned_data)
            print("created user", user)
            return redirect("/register_user")

        else:
            register_form = self.form_class
