from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Tag, Task
from .forms import TaskCreateForm, TaskUpdateForm, UserRegisterForm


@login_required
def home(request):
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(request, "list/home.html", {"tasks": tasks})


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    queryset = Tag.objects.order_by("id")
    context_object_name = "tags"


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all().order_by("is_done", "-created_at")
    context_object_name = "tasks"
    template_name = "list/home.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "list/task_form.html"
    success_url = reverse_lazy("home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = "list/task_form.html"
    success_url = reverse_lazy("home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "list/task_confirm_delete.html"
    success_url = reverse_lazy("home")


class TaskToggleStatusView(generic.View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return redirect("home")


class RegisterView(generic.View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "registration/register.html", {"form": form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            return redirect("login")
        return render(request, "registration/register.html", {"form": form})
