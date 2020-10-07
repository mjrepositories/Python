from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('',views.home_view, name = 'home-page'),
    # path('service',views.create_service, name = 'service-page'),
    ] \
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)