from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.main_menu,name='main_menu'),
    path('export/xlsx/', views.export_template_xls, name='export_template_xls'),
    ]