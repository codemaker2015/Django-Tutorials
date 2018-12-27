from django.db import models

class Employee(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	address = models.CharField(max_length=200)
	contact = models.CharField(max_length=20)
	def __str__(self):
		return self.name