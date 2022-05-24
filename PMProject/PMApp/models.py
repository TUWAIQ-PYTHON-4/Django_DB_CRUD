from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50, help_text=" name Project.")
    creation_time = models.DateTimeField(auto_now_add=True, help_text="creation time")
    completion_time = models.DateTimeField(null=True, help_text="completion time")

    def __str__(self):
        return self.name


class Task(models.Model):

    title = models.CharField(max_length=50, help_text="title the task.")
    description = models.TextField(help_text="the description")
    time_estimate = models.IntegerField(null=True, help_text="estimation time")
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, null = True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
