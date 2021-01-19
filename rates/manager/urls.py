from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home_view, name = 'home_page'),
    path('register',views.register,name = 'register'),
    path('login',auth_views.LoginView.as_view(template_name='manager/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='manager/logout.html'),name='logout'),
    path('about',views.about,name = 'about'),
    path('shipments/<slug:t_type>', views.shipments,name='shipments'),
    path('reporting/<slug:t_type>', views.reporting,name='reporting'),
    path('charts/<slug:t_type>', views.charts,name='charts'),
    path('shipments/notes/<slug:mode>/<slug:shipment>',views.notes,name='notes'),
    path('load_data',views.load_data,name='load_data')
    # below is the standard way of adding static files for app
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)