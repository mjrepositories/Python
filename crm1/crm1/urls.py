"""crm1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""






# This file is responsible for what usering is typing as for url
# When url is added in the browser - this file directs to proper pages

from django.contrib import admin
from django.urls import path,include

# we are importing library that will enable us to get to profile pics
# and it let us work on settings from our application
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # below is telling the server to move us to accounts.urls to handled further routing
    path('',include('accounts.urls'))

]
# first vaiable is saying in which file we go (so whenever we goes to /images
# django should look for graphics in the MEDIA ROOT
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# C:\Users\310295192\Desktop\Python\crm1