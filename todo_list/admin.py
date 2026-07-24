from django.contrib import admin
from django.contrib.auth.models import Group

from todo_list.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "date", "deadline", "is_done")
    search_fields = ("content",)
    list_filter = ("deadline", "is_done")
    list_per_page = 20


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_per_page = 20


admin.site.unregister(Group)
