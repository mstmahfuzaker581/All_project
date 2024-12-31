from django.db import models
from task.models import Task

class TaskCategory(models.Model):
    category_name = models.CharField(max_length=100)
    tasks = models.ManyToManyField(Task, related_name='categories')

    def __str__(self):
        return self.category_name