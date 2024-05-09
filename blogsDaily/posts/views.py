from django.shortcuts import render, redirect
from .models import Post
from .forms import PostModelForm, CommentForm
from authentication.middlewares import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

@auth
def home(request):
    posts = Post.objects.all()
    context={
        'posts' : posts
    }
    return render(request, 'posts/home.html',context)


@auth
def post(request):
    if request.method == 'POST':
        form =PostModelForm(request.POST, request.FILES)
        print(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:home')

    else:
        form = PostModelForm()
    context = {
        'form' : form
    }
    return render(request, 'posts/posts.html', context)

@auth
def blog_page(request, url):
    post= Post.objects.get(url=url)
    if request.method == 'POST':
        comment_form =CommentForm(request.POST)
        if comment_form.is_valid():
            instance= comment_form.save(commit=False)
            instance.commented_on = post
            instance.save()
            return redirect('posts:blog_page', url=post.url)
    else:
        comment_form=CommentForm()
    context ={
        'post':post,
        'comment_form':comment_form,
    }
    return render(request, 'posts/blog_page.html', context )

@auth
def about(request):
    return render(request, 'posts/about.html')

@auth
def profile(request):
    user = request.user
    context ={
        'user': user
    }
    return render(request, 'posts/profile.html', context)

@auth
def contact(request):
    return render(request, 'posts/contact.html')


@auth
def modify_profile(request):
    return render(request, 'posts/modify_profile.html')


@auth
def suggest_gpt(request):
    return render(request, 'posts/suggest_gpt.html')