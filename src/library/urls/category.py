from django.urls import re_path
from ..views import (
    ResourceCategoriesListCreateView,
    CategoryDetailUpdateView,
    ResourceCategoryDeleteView,
)

urlpatterns = [
    re_path(
        r"$",
        ResourceCategoriesListCreateView.as_view(),
        name="resource_categories",
    ),
    re_path(
        r"(?P<pk>\d)/delete/$",
        ResourceCategoryDeleteView.as_view(),
        name="delete_resource_category",
    ),
    re_path(
        r"(?P<id>\d)/detail/$",
        CategoryDetailUpdateView.as_view(),
        name="resource_category_detail",
    ),
]
