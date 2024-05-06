from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse



# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 8:
            messages.error(request, 'password should contain atleast 8 characters')
            return redirect('authentication:signUp')

        users = User.objects.filter(username=username)
        if users:
            messages.error(request, 'username already exists')
            return redirect('authentication:signUp')
        
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
    return render(request, 'authentication/sign_up.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        is_user_valid =authenticate(username=username, password=password)
        if is_user_valid is not None:
            login(request, is_user_valid)
            return redirect('posts:home')
        else:
            messages.error(request, 'wrong user credentials')
            return redirect('authentication:signIn')

    return render(request, 'authentication/sign_in.html')

def sign_out(request):
    logout(request)
    return redirect(reverse('authentication:signIn'))
