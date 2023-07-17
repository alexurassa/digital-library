from django.urls import re_path
from ..views import (
    ResourceTypesListCreateView,
    ResourceTypeDeleteView,
    ResourceTypeDetailUpdateView,
)


urlpatterns = [
    re_path(r"$", ResourceTypesListCreateView.as_view(), name="resource_types"),
    re_path(
        r"(?P<pk>\d)/delete/$",
        ResourceTypeDeleteView.as_view(),
        name="delete_resource_type",
    ),
    re_path(
        r"(?P<pk>\d)/detail/$",
        ResourceTypeDetailUpdateView.as_view(),
        name="resource_type_detail",
    ),
]
