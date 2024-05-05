from django.shortcuts import render, redirect
from .models import Post
from .forms import PostModelForm, CommentForm

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


def blog_page(request, url):
    post= Post.objects.get(url=url)
    if request.method == 'POST':
        comment_form =CommentForm(request.POST)
        if comment_form.is_valid():
            instance= comment_form.save(commit=False)
            instance.commented_on = post
            instance.save()
            return redirect('posts:blog_page', pk=post.postId)
    else:
        comment_form=CommentForm()
    context ={
        'post':post,
        'comment_form':comment_form,
    }
    return render(request, 'posts/blog_page.html', context )


def about(request):
    return render(request, 'posts/about.html')

def profile(request):
    return render(request, 'posts/profile.html')

def contact(request):
    return render(request, 'posts/contact.html')
