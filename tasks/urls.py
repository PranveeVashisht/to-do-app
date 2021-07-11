from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('update/<int:pk>/', views.updateTask, name="update_task"),
    path('delete/<int:pk>/', views.deleteTask, name="delete_task"),
    path('cross/<int:pk>/', views.crossTask, name="cross_task"),
    path('uncross/<int:pk>/', views.uncrossTask, name="uncross_task"),
    path('projects/', views.projects, name="projects")
]