from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from teams.models import BasicTeam

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect(reverse('home'))
        else:
            messages.error(request, "form is not valid")
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'registration/register_user.html', {'form': form})

@login_required(login_url='/users/login/')
def user_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user) ## denver
        print(f"fav:{profile.favorite_team.full_name}")
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()
    finally:
        print('finally')
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
        else:
            form = UserProfileForm(instance=profile)
    print('return')
    return render(request, 'registration/user_profile.html', context={'form':form})


