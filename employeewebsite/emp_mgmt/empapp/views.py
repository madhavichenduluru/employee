from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from empapp.models import Employee
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class EmployeeListView(ListView):
    model = Employee


class EmployeeDetail(DetailView):
    model = Employee


class EmployeeCreateView(CreateView):
    model = Employee
    fields = ('employeeid','name','description','email','position','hiringdate','created_by')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ('name','description','email','position')
    success_url = "/empapp"

from django.urls import reverse_lazy
class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee_list')
