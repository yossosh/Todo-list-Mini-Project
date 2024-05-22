from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Tag, Task


@login_required
def home(request):
    """View function for the home page of the site."""
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(
        request,
        "list/home.html",
        {
            "tasks": tasks,
            "num_visits": num_visits,
        },
    )
