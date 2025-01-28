from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    marks = models.IntegerField()

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)

def __str__(self):
    return self.ename