from django.db import models

from django.contrib.auth.models import User
# Create your models here.

'''
 What are models?
 Python classes that inherit from Django  models and allows  us to create classes that represent
 database tables 
'''


''''
signals are comprised of senders and receivers. Something is being sent to the receiver when action occurs
'''
class Customer(models.Model):

    # on_delete tells us how system should work in case of deleting a user
    # in this case it is telling the system that user should be deleted
    #whenever a user is deleted we will delete this relationship
    #OnetoOneFIeld means that user can have one user and customer can have one user
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    #blank True means that we can create customer without user attached
    # We inherit from models.Model
    # we have to give it a first attribute - which will be a customer name
    # we have to then specify the type of the data for database
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null =True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="logo.png",null=True,blank=True)
    # DateTimeField will indicated when  the object was created
    date_created=models.DateTimeField(auto_now_add=True)
    # specifying null value will allow us to pull the data from the database without any error
    # otherwise - we would need to put there some default values

    # after creating such table we have to migrate it to the database so that we have up-to-date tables

    # below is returing the name of the person in the database instead of having it as an object 1
    def __str__(self):
        return self.name


# below will be the tag for products like sport, cooking, lifestyle, etc.
class Tag(models.Model):

    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name



class Product(models.Model):
     # indictaing the categories and statuses allows us to create values for drop dwon llists
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
     # below is creating the many to many connection between two models
     # so that one tag could have many proucts and one product could have many tags
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered',' Delivered'),

    )
    # on_delete tells us what should be done with the order when value
    # described is deleted
    # SET_NULL tells django to replace this value with NULL
    # CASCADE would tell django to delete the whole entry
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    # we are setting up by below a custom attribute
    note = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.product.name


#Quering models
'''
queryset =  Customer.objects.all()

queryset here is the variable that is holding the return value from the function that we use
Customer is the model/table that holds the data we are going to check
objects is the Model Objects attribute that we would like to extract from our model/table
all() is one of the function that we can used on specific model 
there are also other functions like get() which extract one value
or filter() which filters out the data based on the fileter we input
'''

"""
{%%}
braces with percent signs
this sign allows us to write python logic in templates so that we can use loop, if statements, etc

{{}}
double braces
allows us to access data as for variables
"""