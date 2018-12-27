from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30,unique=True)
    age=models.IntegerField(default=0)
    tot=models.IntegerField(default=0)
    def __str__(self):
        return self.name+"details added"
class Mark(models.Model):
    result = models.DateTimeField('date published')
