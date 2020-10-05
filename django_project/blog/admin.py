from django.contrib import admin
from .models import Post
# Register your models here.

# below allows to register the Post model/table from the database to be seen on admin page level
admin.site.register(Post)
