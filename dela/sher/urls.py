from django.urls import path
from . import views


# futher processing the routing from main urls
urlpatterns = [
    path('', views.home,name='home-page'),
    path('about/',views.about,name='about-page'),
    path('offers/',views.offers,name='offers-page')

]
