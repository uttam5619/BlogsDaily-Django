from django.shortcuts import render, redirect
from .forms import TodoModelForm
from django.contrib.auth.decorators import login_required
from authentication.middlewares import auth
from .models import todo

# Create your views here.

@auth
def todo_form(request):
    if request.method == 'POST':
        form =TodoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:home')

    else:
        form = TodoModelForm()
    context = {
        'form' : form
    }
    return render(request, 'todos/todo_form.html', context)

@auth
def todo_list(request):

    user = request.user
    todos = todo.objects.filter(user=user)
    context ={
        'todos': todos,
        'user' : user
    }
    return render(request, 'todos/todo_list.html',context)

@auth
def delete_todo(request):
    pass

@auth
def update_todo(request):
    pass