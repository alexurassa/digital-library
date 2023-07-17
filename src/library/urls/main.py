from django.urls import re_path, include


app_name: str = "library"

urlpatterns = [
    re_path(r"resources/", include("library.urls.resource")),
    re_path(
        r"resource-categories/",
        include("library.urls.category"),
    ),
    re_path(
        r"authors/",
        include("library.urls.author"),
    ),
    re_path(
        r"borrows/",
        include("library.urls.borrowed_resources"),
    ),
    re_path(
        r"resource-types/",
        include("library.urls.resource_type"),
    ),
]
