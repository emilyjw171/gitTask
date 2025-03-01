from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Song


# Homepage
def home(request):
    """
    Renders the homepage of the website.

    Args:
        request (HttpRequest): The request object containing metadata about 
        the request.

    Returns:
        HttpResponse: The rendered homepage template (band/home.html).
    """
    return render(request, 'band/home.html')


# Band Members
def band_members(request):
    """
    Renders the page displaying band members.

    Args:
        request (HttpRequest): The request object containing metadata about 
        the request.

    Returns:
        HttpResponse: The rendered band members template (band/members.html).
    """
    return render(request, 'band/members.html')


# Album Page
def album(request):
    """
    Renders the album page with a list of all songs.

    Args:
        request (HttpRequest): The request object containing metadata about 
        the request.

    Returns:
        HttpResponse: The rendered album template (band/album.html), 
                      including all songs in the database.
    """
    songs = Song.objects.all()
    return render(request, 'band/album.html', {'songs': songs})


def register(request):
    """
    Handles user registration and login.

    If the request is a POST, it processes the form data for user creation and 
    logs in the user.
    If the request is GET, it displays the registration form.

    Args:
        request (HttpRequest): The request object containing metadata about 
        the request.

    Returns:
        HttpResponse: Redirects to the homepage after successful registration 
        or renders the registration page if the form is invalid.
    """
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
