from django.db import models
from empapp.models import Employee

# Create your models here.

class Leave(models.Model):
    leaveid = models.CharField(max_length=50)
    emp = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employees')
    start_date = models.DateField()
    end_date = models.DateField()
    leave_status = [
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
    ]
    leave_status = models.CharField(max_length=10, choices=leave_status, default='pending')
    reason = models.CharField(max_length=100)
    file_name = models.CharField(max_length=255)
    my_file = models.FileField(upload_to='')
