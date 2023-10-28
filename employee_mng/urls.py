from django.urls import path
from . import views

urlpatterns = [
    path('add/new/', views.EmployeeOperations.as_view(), name='add_new_employee'),
    path('get/all/', views.EmployeeOperations.as_view(), name='get_all_employees'),
]