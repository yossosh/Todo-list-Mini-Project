from django.urls import path

from .views import (
    home,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleStatusView,
    RegisterView,
)

app_name = "list"

urlpatterns = [
    path("", home, name="home"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("task/add/", TaskCreateView.as_view(), name="add_task"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="update_task"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="delete_task"),
    path(
        "task/<int:pk>/toggle/",
        TaskToggleStatusView.as_view(),
        name="toggle_task_status",
    ),
]
