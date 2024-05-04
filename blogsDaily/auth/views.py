from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signUp(request):
    return render(request, 'auth/signUp.html')

def signIn(request):
    return render(request, 'auth/signIn.html')