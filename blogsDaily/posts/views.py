from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'posts/home.html')

def post(request):
    return render(request, 'posts/post.html')

def about(request):
    return render(request, 'posts/about.html')

def profile(request):
    return render(request, 'posts/profile.html')

def contact(request):
    return render(request, 'posts/contact.html')
