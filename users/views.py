from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm()
        if form.is_valid():
            form.save()
        return redirect(reverse('home'))
    
    else:
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})