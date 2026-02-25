from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):
    task = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # Add owner field to associate tasks with users
    
    def __str__(self):
        return self.task + " - " + str(self.done)