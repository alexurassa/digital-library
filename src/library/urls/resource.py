from django.urls import re_path, include
from ..views import (
    ResourcesListCreateView,
    ResourceDetailUpdateView,
    ResourceDeleteView,
)


urlpatterns = [
    re_path(r"$", ResourcesListCreateView.as_view(), name="resources"),
    re_path(r"checklist/", include("library.urls.checklist")),
    re_path(
        r"(?P<pk>[\w-]{20})/detail/$",
        ResourceDetailUpdateView.as_view(),
        name="resource_detail",
    ),
    re_path(
        r"(?P<pk>[\w-]{20})/delete/$",
        ResourceDeleteView.as_view(),
        name="delete_resource",
    ),
]
