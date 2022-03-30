from django.contrib import admin
from . models import Leave

# Register your models here.
class LeaveAdmin(admin.ModelAdmin):
    list_display = ['leaveid','emp','start_date','end_date']
admin.site.register(Leave,LeaveAdmin)
