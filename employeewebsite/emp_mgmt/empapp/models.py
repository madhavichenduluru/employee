from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Employee(models.Model):
    employeeid = models.CharField(max_length=16)
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=200)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    hiringdate = models.DateField()
    created_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('employee_list')
