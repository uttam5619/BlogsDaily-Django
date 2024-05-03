from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('todo_registration', views.todo_form, name='todo_form' ),
    path('markList', views.todo_list, name='todo_list' ),
]
