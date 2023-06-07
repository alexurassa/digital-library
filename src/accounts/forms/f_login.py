from typing import Any, Dict
from django import forms
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    """A form that carries a login payload"""

    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
