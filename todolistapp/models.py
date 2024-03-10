from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#create basic model
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False) # <--- added
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
