from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
from .models import TaskList
from .form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required   
    

@login_required # Decorator to require login for accessing the index view
def index(request):
    today = datetime.date.today() # Get the current date
    if request.method == "POST":
        form = TaskForm(request.POST or None) # Create a form instance with the POST data
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, "Task added successfully!")
            return redirect('index') # Redirect to the index page after saving the task
    else:
        form = TaskForm() # Create an empty form instance for GET requests
    
    all_tasks = TaskList.objects.filter(owner=request.user) # Get all tasks from the database that belong to the current user
    paginator = Paginator(all_tasks, 3) # Create a paginator with 3 tasks per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "day": today,
        "form": form,
        "page_obj": page_obj
    }

    return render(request, 'todolist_app/index.html', context) # Render the index.html template with the context containing the current date, form, and paginated tasks

@login_required 
def about(request):
    return render(request, 'todolist_app/about.html',{})

@login_required 
def contact(request):
    return render(request, 'todolist_app/contact.html',{})

@login_required 
def delete_task(request, task_id):
    task = TaskList.objects.get(id=task_id) # Get the task to be deleted by its ID
    if task.owner != request.user: # Check if the task belongs to the current user
        messages.error(request, "You are not authorized to delete this task.")
        return redirect('index') # Redirect to the index page if the user is not authorized
    
    task.delete() # Delete the task from the database
    messages.success(request, "Task deleted successfully!")
    return redirect('index') # Redirect to the index page after deleting the task

@login_required 
def edit_task(request, task_id):
    task = TaskList.objects.get(id=task_id) # Get the task to be edited by its ID
    if request.method == "POST":
        form = TaskForm(request.POST or None, instance=task) # Create a form instance with the POST data and the existing task
        if form.is_valid():
            form.save() # Save the updated task to the database
        messages.success(request, "Task updated successfully!")
        return redirect('index') # Redirect to the index page after updating the task
    
    return render(request, 'todolist_app/edit.html', {"task": task})

def home(request):
    return render(request, 'todolist_app/home.html',{})