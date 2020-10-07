from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50, null=True)


    def __str__(self):
        return f'{self.user.username} Profile'


class Item(models.Model):
    owner = models.ForeignKey(Profile,null = True,on_delete=models.CASCADE)
    thing = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=1000,null=True)
    time_registered = models.DateField(default=timezone.now)