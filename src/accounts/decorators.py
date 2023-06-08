from django.http import HttpRequest
from django.shortcuts import redirect
from django.conf import settings


def allowToLogin(view_func):
    """Allows unauthenticated users to login while preventing authenticated users"""

    def wrapper(request: HttpRequest, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect(settings.LOGIN_REDIRECT)

    return wrapper
