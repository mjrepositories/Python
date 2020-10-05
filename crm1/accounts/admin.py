from django.contrib import admin

# Register your models here.

# below we importer the model/table that we will add to the admin panel so that it can be managed there
from .models import *

# we are adding table to admin page
admin.site.register(Customer)

admin.site.register(Product)

admin.site.register(Order)

admin.site.register(Tag)