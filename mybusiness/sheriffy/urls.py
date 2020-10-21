from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import OfferListView,ItemDeleteView,ItemUpdateView,ItemCreate





urlpatterns = [
    path('',views.home_view, name = 'home-page'),
    path('register',views.register,name = 'register'),
    path('login',auth_views.LoginView.as_view(template_name='sheriffy/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='sheriffy/logout.html'),name='logout'),
    path('offers',OfferListView.as_view(template_name='sheriffy/my_offers.html'), name = 'offers'),
    path('create_item',views.ItemCreate, name = 'create_item'),
    path('repair/<int:pk>/update', views.ItemUpdateView.as_view(), name='item-update'),
    path('repair/<int:pk>/delete', views.ItemDeleteView.as_view(), name='item-delete')
    # path('service',views.create_service, name = 'service-page'),
    ] \
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)