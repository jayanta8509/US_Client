from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Todolist(models.Model):
#     user = models.ForeignKey(User , on_delete=models.SET_NULL,null=True,blank=True)
#     date = models.DateField(null=True)
#     text = models.TextField(null=True)