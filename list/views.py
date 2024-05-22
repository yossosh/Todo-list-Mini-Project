from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tag, Task

@login_required
def home(request):
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(request, "list/home.html", {"tasks": tasks})


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    queryset = Tag.objects.order_by("id")
    context_object_name = "tags"
