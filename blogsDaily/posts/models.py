from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=250, default='title')
    descriptions=models.CharField(max_length=500, default='description', blank=True)
    url=models.CharField(max_length=150)
    image=models.ImageField(upload_to='category/')

    def __str__(self):
        return self.title

class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    title=models.CharField(max_length=250)
    subject=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    descriptions=models.TextField()
    url=models.CharField(max_length=150)
    image=models.ImageField(upload_to='post/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



