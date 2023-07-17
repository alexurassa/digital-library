from django.urls import re_path

from ..views import ChecklistItemDetailView, ResourcesChecklistView


urlpatterns = [
    re_path(r"$", ResourcesChecklistView.as_view(), name="resources_checklist"),
    re_path(
        r"(?P<pk>[\w-]{20})/detail/$",
        ChecklistItemDetailView.as_view(),
        name="checklist_item_detail",
    ),
]
