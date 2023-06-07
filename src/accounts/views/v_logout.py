from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect


class LogoutView(View):
    """Logout `User` from the current request"""

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "You are successfully logged out")
        return redirect("/")
