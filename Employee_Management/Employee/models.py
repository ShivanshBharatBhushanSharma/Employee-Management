from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=20, null=False, blank=True)
    Department = models.CharField(max_length=20)
    Designation = models.CharField(max_length=20)
    Salary = models.IntegerField()    
    Hiring_date = models.DateField()   
