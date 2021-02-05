from django.urls import path
from .views import article_list,apiOverview,article_detail


urlpatterns = [
    path('article/', article_list,name='article_list'),
    path('overview/',apiOverview,name='api_view'),
    path('article/<int:pk>',article_detail,name='article_detail')
]