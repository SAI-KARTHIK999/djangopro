from django.db import models

class Student(models.Model):
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=10)
    cie = models.IntegerField()