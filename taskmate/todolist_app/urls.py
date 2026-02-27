from . import views
from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('api/tasks/', TaskListCreateView.as_view(), name='api-tasks'), # Add this line to include the API endpoint for tasks
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='api-task-detail'), # Add this line to include the API endpoint for task details
]
