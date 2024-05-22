from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Tag, Task
from .forms import TaskCreateForm, TaskUpdateForm, TagForm


@login_required
def home(request):
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(request, "list/home.html", {"tasks": tasks})


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    queryset = Tag.objects.order_by("id")
    context_object_name = "tags"
    template_name = "list/tag_list.html"


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.all().order_by("is_done", "-created_at")
    context_object_name = "tasks"
    template_name = "list/home.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "list/task_form.html"
    success_url = reverse_lazy("list:home")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = "list/task_form.html"
    success_url = reverse_lazy("list:home")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "list/task_confirm_delete.html"
    success_url = reverse_lazy("list:home")


class TaskToggleStatusView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return redirect("list:home")


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "list/tag_form.html"
    success_url = reverse_lazy("list:tag_list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "list/tag_form.html"
    success_url = reverse_lazy("list:tag_list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    template_name = "list/tag_confirm_delete.html"
    success_url = reverse_lazy("list:tag_list")
