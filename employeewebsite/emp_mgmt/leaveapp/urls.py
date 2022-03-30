from django.urls import path

from . import views

urlpatterns = [
  path('',views.leavehome,name='leave_home'),
  path('applyleave/',views.leaveupload,name='leave_upload'),
  path('displayleaves/',views.showleaves,name='show_leaves'),
  path('deleteleaves/<int:id>',views.deleteleave,name='delete_leave'),
  path('approveleaves/<int:id>',views.approveleave,name='approve_leave'),
  path('rejectleaves/<int:id>',views.rejectleave,name='reject_leave'),
  path('dataleaves/',views.dataview,name='data_leave'),

]
