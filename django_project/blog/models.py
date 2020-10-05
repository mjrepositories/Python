# in models we want to think what we would like to store in our database
from django.db import models
# by importing utils we can get to some utilities that can be further used
# while creating some additional features
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import  reverse


# Create your models here.

# class post is a table in data base that is related to post
# that will be posted on the website
# in general - those attributes that are set up under the class
# these are just columns in our database table
class Post(models.Model):
    # models.Charfield is a field on the website that we can restrict
    # as for the number of caracters
    title = models.CharField(max_length=100)
    #Textfield is a field that can have many characters in itself
    content = models.TextField()
    # Datetime field is used to store datetime data
    # timezone is a function but we want to execute it at this time
    date_posted = models.DateTimeField(default=timezone.now)
    # we type in the table that is connected with the post table so author of the posts
    # on delete option indicates what we want to do if table for user is deleted
    # models.CASCADE causes the post table to delete the post as well
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# User.objets.all() will generate the query set of all users
# User.objects.first() will  generate value  with first user
#User.objects.filter(filter) will cause filtering of the data

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})