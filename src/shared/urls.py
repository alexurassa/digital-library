from django.urls import re_path

from .views import HomePageView

app_name: str = "shared"


urlpatterns = [re_path(r"$", HomePageView.as_view(), name="homepage")]
