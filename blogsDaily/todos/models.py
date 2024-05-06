from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    subject = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=300, blank=True)
    crux = models.CharField(max_length=350, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title