from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Song


# Homepage
def home(request):
    return render(request, 'band/home.html')


# Band Members
def band_members(request):
    return render(request, 'band/members.html')


# Album Page
def album(request):
    songs = Song.objects.all()
    return render(request, 'band/album.html', {'songs': songs})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'band/register.html', {'form': form})
