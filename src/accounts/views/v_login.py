from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings
from django.utils.decorators import method_decorator
from ..forms import LoginForm

from ..decorators import allowToLogin


class LoginView(View):
    template_name = "auth/login.html"
    form_class = LoginForm

    @method_decorator(allowToLogin)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"login_form": form})

    def post(self, request, *args, **kwargs):
        login_form = self.form_class(request.POST)
        if login_form.is_valid():
            user = authenticate(
                request,
                email=login_form.cleaned_data["email"],
                password=login_form.cleaned_data["password"],
            )
            if user:
                login(request, user)
                messages.success(
                    request, f"Hi {user.first_name}, you are successfully logged in."
                )
                return redirect(settings.LOGIN_REDIRECT)
            else:
                messages.error(request, "Invalid credentials")
                return redirect(settings.LOGIN_URL)
        else:
            messages.error(request, "Invalid credentials")
            return redirect(settings.LOGIN_URL)
