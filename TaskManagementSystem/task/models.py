from django.db import models

class Task(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle