from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

from todo_list.models import Task, Tag


class TaskListView(ListView):
    model = Task
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.prefetch_related("tags")


class TaskChangeStatusView(View):
    def post(self, request, pk, **kwargs):
        task = get_object_or_404(Task, pk=pk)

        task.is_done = not task.is_done
        task.save()

        return redirect("todo_list:index")


class TagListView(ListView):
    model = Tag
    paginate_by = 10

