from django.urls import path

from todo_list.views import TaskListView, TagListView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tags_list"),
]

app_name = "todo_list"
