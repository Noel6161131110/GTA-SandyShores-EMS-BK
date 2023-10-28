from django.urls import path
from . import views

urlpatterns = [
    path('auth/create/', views.UserAuth.as_view(), name='create_user'),
    path('auth/get_all/', views.UserAuth.as_view(), name='get_all_users'),
    path('auth/login/', views.UserLogin.as_view(), name='login'),
    path('promote/employee/', views.EmployeePromote.as_view(), name='promote_employee'),
    path('promote/filter/employee/', views.GetEmployeeFiveYear.as_view(), name='get_employee_five_year'),
]