from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from tasks.forms import TaskForm, TagForm
from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = "task"
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("tasks:task-list")


def task_set_complete(request, pk):
    task = Task.objects.get(id=pk)
    task.is_complete = True
    task.save()
    return redirect("tasks:task-list")


def task_set_not_complete(request, pk):
    task = Task.objects.get(id=pk)
    task.is_complete = False
    task.save()
    return redirect("tasks:task-list")


class TagListView(ListView):
    model = Task
    context_object_name = "tags"
    template_name = "tasks/tag_list.html"
    queryset = Tag.objects.all()


class TagCreateView(CreateView):
    form_class = TagForm
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    context_object_name = "tag"
    template_name = "tasks/tag_delete.html"
    success_url = reverse_lazy("tasks:tag-list")
