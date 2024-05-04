from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = 'authentication'

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    
]