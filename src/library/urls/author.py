from django.urls import re_path
from ..views import AuthorsListCreateView, AuthorDetailUpdateView, AuthorDeleteView

urlpatterns = [
    re_path(r"$", AuthorsListCreateView.as_view(), name="authors_list_create"),
    re_path(
        r"(?P<pk>\w{20})/detail/$",
        AuthorDetailUpdateView.as_view(),
        name="author_detail",
    ),
    re_path(
        r"(?P<pk>\w{20})/delete/$",
        AuthorDeleteView.as_view(),
        name="delete_author",
    ),
]
