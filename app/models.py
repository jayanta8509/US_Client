from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Nameoffile(models.Model):
    user_id = models.BigIntegerField(null=True)  # This field is used to store the id of the user who uploaded this
    user_name = models.CharField(max_length= 250,null=True)
    file_name  = models.CharField(max_length= 250,null=True)
    image = models.FileField(null=True)
    date = models.DateField(auto_now_add=True,null=True)