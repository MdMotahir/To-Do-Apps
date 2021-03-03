from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

# Create your models here.

class Task(models.Model):
    user=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    task=models.CharField(max_length=150)
    description=models.TextField()
    task_date=models.DateTimeField()
    due_date=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return self.task
    