from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    doj = models.DateField()   # Date of Hiring
    job = models.CharField(max_length=50)
    salary = models.IntegerField()