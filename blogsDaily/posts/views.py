from django.shortcuts import render, redirect
from .models import Post
from .forms import PostModelForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context={
        'posts' : posts
    }
    return render(request, 'posts/home.html',context)


def post(request):
    if request.method == 'POST':
        form =PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PostModelForm()
    context = {
        'form' : form
    }
    return render(request, 'posts/posts.html', context)


def about(request):
    return render(request, 'posts/about.html')

def profile(request):
    return render(request, 'posts/profile.html')

def contact(request):
    return render(request, 'posts/contact.html')
