from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from todo_list.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "is_done", "tags")
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
            "tags": forms.CheckboxSelectMultiple(),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        if deadline and deadline < timezone.now():
            raise ValidationError("Deadline cannot be in the past")
        return deadline
