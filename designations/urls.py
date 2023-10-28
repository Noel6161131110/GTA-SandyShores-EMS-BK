from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.DesignationView.as_view()),
    path('get_all/', views.DesignationView.as_view()),
]