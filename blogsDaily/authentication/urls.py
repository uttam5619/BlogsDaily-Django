from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('signUp/', views.sign_up, name='signUp' ),
    path('signIn/', views.sign_in, name='signIn' ),
    path('signOut/', views.sign_out, name='signOut')
]
