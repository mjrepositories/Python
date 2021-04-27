from django.db import models

# Create your models here.

class Cart(models.Model):
    producer = models.CharField(max_length=10,null=True,blank=True)