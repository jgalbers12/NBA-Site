from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm()
        if form.is_valid():
            form.save()
        return redirect(reverse('home'))
    
    else:
        form = UserCreationForm()
        return render(request, 'registration/register_user.html', {'form': form})