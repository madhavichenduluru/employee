from django.urls import path
from empapp import views
from django.conf.urls import url


#app_name = 'empapp'
urlpatterns = [

    path('', views.EmployeeListView.as_view(), name='employee_list'),
    path('<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),
    path('create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('update/<int:pk>', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('delete/<int:pk>', views.EmployeeDeleteView.as_view(), name='employee_delete'),
]
