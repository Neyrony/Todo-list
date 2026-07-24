from django.views.generic import ListView

from todo_list.models import Task, Tag


class TaskListView(ListView):
    model = Task
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.prefetch_related("tags")


class TagListView(ListView):
    model = Tag
    paginate_by = 10

