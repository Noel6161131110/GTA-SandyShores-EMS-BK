from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.DepartmentFn.as_view(), name='department_create'),
]