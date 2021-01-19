from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home_page, name = 'home-page'),
    path('register_cost_home',views.register_cost_home,name='register-cost-home'),
    path('register_cost_energy',views.register_cost_energy,name='register-cost-energy'),
    path('register_cost_gas',views.register_cost_gas,name='register-cost-gas'),
    path('register_cost_tv',views.register_cost_tv,name='register-cost-tv'),
    path('register_cost_internet',views.register_cost_internet,name='register-cost-internet'),
    path('check_cost_home',views.cost_home,name='check-cost-home'),
    path('check_cost_energy',views.cost_energy,name='check-cost-energy'),
    path('check_cost_gas',views.cost_gas,name='check-cost-gas'),
    path('check_cost_tv',views.cost_tv,name='check-cost-tv'),
    path('check_cost_internet',views.cost_internet,name='check-cost-internet'),
    path('update_bill/<slug:group>/<slug:id>',views.correct_cost,name='update-cost')
                  # below is the standard way of adding static files for app
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)