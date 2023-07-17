from django.urls import re_path

from ..views import (
    BorrowedResourcesListView,
    BorrowedResourceDetailUpdateView,
    DeleteBorrowedResourceView,
)


urlpatterns = [
    re_path(r"$", BorrowedResourcesListView.as_view(), name="borrowed_resources"),
    re_path(
        r"(?P<pk>[\w-]{20})/detail/$",
        BorrowedResourceDetailUpdateView.as_view(),
        name="borrowed_resource_detail",
    ),
    re_path(
        r"(?P<pk>[\w-]{20})/delete/$",
        DeleteBorrowedResourceView.as_view(),
        name="delete_borrowed_resource",
    ),
]
