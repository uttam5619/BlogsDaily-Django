from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home' ),
    path('profile/', views.profile, name='profile' ),
    path('post/', views.post, name='post' ),
    path('about/', views.about, name='about' ),
    path('contact/', views.contact, name='contact')
]
