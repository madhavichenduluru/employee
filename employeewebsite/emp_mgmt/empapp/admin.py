from django.contrib import admin
from empapp.models import Employee

# Register your models here.
#class EmployeeAdmin(admin.ModelAdmin):
#    list_display = ['employeeid','name','description','email']

#admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Employee)
