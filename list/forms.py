from django import forms

from .models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Task Content"})
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]


class TaskUpdateForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Task Content"})
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )
    is_done = forms.BooleanField(required=False)

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags", "is_done"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
