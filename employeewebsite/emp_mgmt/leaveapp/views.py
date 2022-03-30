from django.shortcuts import render,redirect
from leaveapp.forms import MyLeaveUploadForm
from django.http import HttpResponse
from leaveapp.models import Leave
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def leavehome(request):
    return render(request, 'leaveapp/leavehome.html')

def showleaves(request):
    leaves = Leave.objects.all()
    return render(request,'leaveapp/showleaves.html',{'leaves':leaves})

def leaveupload(request):
    #form = MyLeaveUploadForm()
    form = MyLeaveUploadForm(request.POST or None)
    if request.method == 'POST':
        leave_form = MyLeaveUploadForm(request.POST,request.FILES)

        if leave_form.is_valid():
            leave_form.save()

            return redirect('/leaveapp/displayleaves')
    
    return render(request,'leaveapp/leaveapplication.html',{'form':form})


def deleteleave(request,id):
    leave = Leave.objects.get(id=id)
    leave.delete()
    return redirect('/leaveapp/displayleaves')

def approveleave(request,id):
    leave = Leave.objects.get(id=id)
    leave.leave_status='approved'
    leave.save()
    return redirect('/leaveapp/displayleaves')


def rejectleave(request,id):
    leave = Leave.objects.get(id=id)
    leave.leave_status='rejected'
    leave.save()
    return redirect('/leaveapp/displayleaves')

from django.db.models import Count
def dataview(request):
    #leaves = Leave.objects.all()
    #leaves=Leave.objects.filter(emp__email__exact='smith@gmail.com')
    emaildata=request.GET['emailsearch']
    leaves=Leave.objects.filter(emp__email__contains=emaildata)

    my_dict = {'leaves':leaves}
    return render(request, 'leaveapp/data.html',my_dict)
