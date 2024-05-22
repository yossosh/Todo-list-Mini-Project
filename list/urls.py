from django.urls import path

from .views import (
    home,
)

app_name = "list"

urlpatterns = [
    path("", home, name="home"),
]
