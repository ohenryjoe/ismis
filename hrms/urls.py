from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib import admin
from django.urls import path
from hrms import views
from django.conf.urls import url
from django.urls import include, path

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('Employees', views.employees, name='viewemployees'),
    path('NewEmployee', views.EmployeesCreateView.as_view(), name='employee_add'),
    path('NewDesignation', views.New_Designation, name='new_designation'),
    path('NewDesignation#finish', views.New_Designation, name='new_designation2'),
    path('<int:pk>/', views.EmployeesUpdateView.as_view(), name='employee_change'),
    path('area/directorates/<int:pk>', views.directorate_list, name='list_directorates'),
    path('area/departments/<int:pk>', views.department_list, name='list_departments'),
    path('area/divisions/<int:pk>', views.division_list, name='list_divisions'),
    path('area/designations/<int:pk>', views.designation_list, name='list_designations'),
    path('area/sections/<int:pk>', views.section_list, name='list_sections'),
]


