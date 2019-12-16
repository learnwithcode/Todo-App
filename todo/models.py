from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, 
													null=True, 	
														blank=True, 
															related_name='todo')
	task = models.CharField(max_length=100, null=True, blank=True)


	def __str__(self):
		return self.task
