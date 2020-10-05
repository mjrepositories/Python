from django.urls import path
from . import views
from .views import TicketListView,TicketDetailView,TicketUpdateView,TicketDeleteView

urlpatterns = [
    path('',views.register,name = 'keyuser-home'),
    # class based view has to be converted into view by typing as_view() and executed thus ()

    # below we are directing to view for the ticket, pk is the primary key of the ticket raised and is going
    # to be passed into address so that we will be able to pull proper ticket
    path('ticket/<int:pk>/update',views.TicketUpdateView.as_view(),name = 'ticket-update'),

    # django is looking for <app>/<model>_<viewtype>.html

    path('manager',views.TicketListView.as_view(),name = 'keyuser-overview'),

    path('ticket/<int:pk>/delete',views.TicketDeleteView.as_view(),name = 'ticket-delete'),
]
