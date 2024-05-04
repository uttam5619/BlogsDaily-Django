from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .forms import SignUpForm

# Create your views here.

def sign_in(request):
    return render(request, 'authentication/signIn.html')

def sign_up(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:home')
    else:
        form =SignUpForm()

    context ={
        'form': form,
    }
    return render(request, 'authentication/signUp.html', context)