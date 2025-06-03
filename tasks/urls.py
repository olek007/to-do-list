from django.urls import path

from tasks.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskUpdateView,
    TaskDeleteView,
    task_set_complete,
    task_set_not_complete,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/set-complete/", task_set_complete, name="task-set-complete"),
    path(
        "tasks/<int:pk>/set-not-complete/",
        task_set_not_complete,
        name="task-set-not-complete",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
app_name = "tasks"
