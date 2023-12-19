from django.db import models
from django.utils import timezone


class ToDoItem(models.Model):
    text = models.CharField(max_length=100)
    due_date = models.DateField(default=timezone.now)
def __str__(self):
    return f"{self.text}: due {self.due_date}"

def get_queryset(self):
    return ToDoItem.objects.filter(due_date__gte=date.today())
