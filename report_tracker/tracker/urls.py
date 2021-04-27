# we are importing path so that we can access specific endpoints
from django.urls import path

# import view of an api (endpoint)
from .views import api_all_status_view,apiOverview,api_single_status_view,api_status_update,api_status_check,api_get_periods,data_for_graphs

urlpatterns = [
    path('',apiOverview,name='api-overview'),
    path('all-statuses',api_all_status_view,name='all-statuses'),
    path('status-detail/<str:pk>',api_single_status_view,name='status-detail'),
    path('status-update/<str:pk>',api_status_update,name='status-update'),
    path('status-check',api_status_check,name='status-check'),
    path('get-periods',api_get_periods,name="get-periods"),
    path('graphs',data_for_graphs,name="graphs")
]