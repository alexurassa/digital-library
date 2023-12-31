from django.urls import re_path

from .views import LoginView, RegisterUserView, LogoutView, LibraryUsersListCreateView

app_name: str = "accounts"

urlpatterns = [
    re_path(r"^login/$", LoginView.as_view(), name="login"),
    re_path(r"^logout/$", LogoutView.as_view(), name="logout"),
    re_path(r"^register/$", RegisterUserView.as_view(), name="register_user"),
    re_path(r"^users/$", LibraryUsersListCreateView.as_view(), name="users"),
]
