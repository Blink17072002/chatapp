from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.db.models import Q


from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .email_backend import EmailBackend




def welcome_page(request):
    context = {}
    return render(request, 'chat/base.html', context)

def Login(request):    # In caps because of the imported auth login function
    page = 'login'

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, email=email, password=password)
                if user is not None:      # To check if the authentication is successful
                    login(request, user)
                    return redirect('room:rooms') # This is in the room.view file
                else:
                    if User.objects.filter(password=password).exists():
                        messages.error(request, 'Invalid email')
                    else:
                        messages.error(request, 'Invalid password') 
            except User.DoesNotExist:
                messages.error(request, 'User does not exist')
        else:
            messages.error(request, 'Please provide both email and password')

    context = {'page': page}
    return render(request, 'chat/sign_up.html', context)


def sign_up(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'Signed up successfully!')
            return redirect('room:rooms')
        else:
            messages.error(request, 'An error occurred when signing up:')

    context = {'form': form}
    return render(request, 'chat/sign_up.html', context)

