from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ProjectFn.as_view(), name='project_create'),
    path('get/all/', views.ProjectFn.as_view(), name='project_get_all'),
    path('delete/', views.ProjectFn.as_view(), name='project_delete'),
    path('update/', views.ProjectFn.as_view(), name='project_update'),
]