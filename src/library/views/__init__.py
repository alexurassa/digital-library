from .v_borrows import (
    BorrowedResourcesListView,
    BorrowedResourceDetailUpdateView,
    DeleteBorrowedResourceView,
)
from .v_resource import (
    ResourcesListCreateView,
    ResourceDetailUpdateView,
    ResourceDeleteView,
)
from .v_resource_category import (
    ResourceCategoriesListCreateView,
    CategoryDetailUpdateView,
    ResourceCategoryDeleteView,
)
from .v_author import AuthorsListCreateView, AuthorDetailUpdateView, AuthorDeleteView
from .v_checklist import ResourcesChecklistView, ChecklistItemDetailView
from .v_resource_type import (
    ResourceTypesListCreateView,
    ResourceTypeDeleteView,
    ResourceTypeDetailUpdateView,
)
