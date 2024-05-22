from django.urls import path

from .views import (
    home,
    TagListView,
)

app_name = "list"

urlpatterns = [
    path("", home, name="home"),
    path("tags/", TagListView.as_view(), name="tag_list"),
]
