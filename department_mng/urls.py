from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.DepartmentFn.as_view(), name='department_create'),
    path('get/all/', views.DepartmentFn.as_view(), name='department_get_all'),
    path('update/', views.DepartmentFn.as_view(), name='department_delete'),
    path('delete/', views.DepartmentFn.as_view(), name='department_update'),
    path('add/employee/', views.AssignDepEmp.as_view(), name='department_get_employee'),
]