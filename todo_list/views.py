from django.views.generic import ListView

from todo_list.models import Task


class TaskListView(ListView):
    model = Task
    paginate_by = 10
