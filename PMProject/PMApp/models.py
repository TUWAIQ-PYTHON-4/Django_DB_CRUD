from django.db import models

class Project(models.Model):
   name = models.CharField(max_length=100, help_text="The name of the Project.")
   creation_time = models.DateTimeField(auto_now_add=True, help_text = "The date and time the project was created.")
   completion_time = models.DateTimeField(null=True, help_text="The date and time the project was completed.")

   def _str_(self):
      return self.name

class Task(models.Model):
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   title = models.CharField(max_length=100, help_text="The Title of the Task.")
   description = models.TextField(help_text = "The description of the Task.")
   time_estimate = models.IntegerField(help_text="The estimate for the Task.")
   completed = models.BooleanField(default=False)

   def _str_(self):
      return self.title