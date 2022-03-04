from django.db import models

class EmployeeContact(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=200)
	message=models.TextField(max_length=1000)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"