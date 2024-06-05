from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField()
    Contact=models.CharField(max_length=200)
    City=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)


class Query(models.Model):
    Email = models.EmailField(max_length=50)
    Query = models.CharField(max_length=50)