from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm()
        if form.is_valid():
            form.save()
        return redirect(reverse('home'))
    
    else:
        form = UserCreationForm()
        return render(request, 'users/register_user.html', {'form': form})
    
class UserLoginView(LoginView):
    # add redirect to user info
    template_name = "users/login.html"
    next_page = redirect(reverse_lazy('home'))