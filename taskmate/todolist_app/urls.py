from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
