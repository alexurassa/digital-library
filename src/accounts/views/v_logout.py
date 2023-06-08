from typing import Any
from django import http
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect


@method_decorator(login_required, name="dispatch")
class LogoutView(View):
    """Logout `User` from the current request"""

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "You are successfully logged out")
        return redirect("/")
