from asyncio import Task
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100, help_text="project name")
    creation_time = models.DateField(help_text="date the project ")
    completion_time = models.DateField(help_text="completion time")

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100, help_text="The title")
    description = models.TextField(help_text="description ")
    date = models.DateField(help_text="Description.")
    time_estimate = models.IntegerField(help_text="time")
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
