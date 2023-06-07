from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import auth
from django.conf import settings

from ..forms import RegisterUserForm


User = auth.get_user_model()


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
            cleaned_data = register_form.cleaned_data

            # create user account
            created_user = User.objects.create_user(
                first_name=cleaned_data.get("first_name"),
                last_name=cleaned_data.get("last_name"),
                email=cleaned_data.get("email"),
                password=cleaned_data.get("password2"),
            )

            if created_user:
                # inform
                messages.success(
                    request,
                    f"Congratulations {created_user.first_name}, your account created successfully",
                )

                # authenticate and login
                auth.authenticate(
                    request,
                    email=cleaned_data.get("first_name"),
                    password=cleaned_data.get("password2"),
                )
                auth.login(request, created_user)
                return redirect(settings.LOGIN_REDIRECT)
            else:
                messages.info(request, "Account not created, please try again")
                return redirect("accounts:register_user")
        else:
            messages.error(request, "Please fill correctly")
            register_form = self.form_class(request.POST)
            return redirect("accounts:register_user")
