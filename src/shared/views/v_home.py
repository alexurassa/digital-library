from django.shortcuts import render
from django.views import View


class HomePageView(View):
    """Renders the application homepage"""

    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
