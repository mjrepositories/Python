from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('',views.home_view, name = 'home-page'),
    path('service',views.create_service, name = 'service-page'),
    path('history',views.check_history, name = 'history-page'),
    path('panel',views.ServiceListView.as_view(template_name='car/panel_page.html'), name = 'panel-page'),
    path('repair/<int:pk>/update',views.RepairUpdateView.as_view(),name = 'repair-update'),
    path('repair/<int:pk>/delete',views.RepairDeleteView.as_view(),name = 'repair-delete'),
    path('service/<int:pk>/update', views.ServiceUpdateView.as_view(), name='service-update'),
    path('service/<int:pk>/delete', views.ServiceDeleteView.as_view(), name='service-delete'),
    path('part_service',views.create_part_or_service,name = 'part-service'),
    path('billing',views.billing,name='billing'),
    path('pdf',views.PDF_generation,name='pdf')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)