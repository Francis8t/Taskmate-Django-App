from pyexpat.errors import messages

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import CustomRegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registration successful!Login to Get Started')
            return redirect('register')  # Redirect to a success page or login page
    else:
        register_form = CustomRegisterForm()
    
    
    return render(request, 'register.html', {'register_form': register_form})