from django.urls import path

from todo_list.views import TaskListView, TagListView, TaskChangeStatusView, TaskCreateView, TaskDeleteView, \
    TaskUpdateView, TagCreateView, TagUpdateView, TagDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tasks/create", TaskCreateView.as_view(), name="task_create"),
    path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/change-status", TaskChangeStatusView.as_view(), name="task_change_status"),
    path("tag/<int:pk>/delete", TaskDeleteView.as_view(), name="task_delete"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/create", TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag_update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag_delete"),
]

app_name = "todo_list"
