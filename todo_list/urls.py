from django.urls import path

from todo_list.views import TaskListView, TagListView, TaskChangeStatusView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/<int:pk>/change-status", TaskChangeStatusView.as_view(), name="task-change-status"),
    path("tags/", TagListView.as_view(), name="tags_list"),
]

app_name = "todo_list"
