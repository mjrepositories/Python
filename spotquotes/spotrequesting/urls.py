from django.urls import path
from . import views
from .views import SpotListView,OfferListView,OfferDeleteView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',SpotListView.as_view(), name = 'spot-home'),
    path('offers',OfferListView.as_view(template_name='spotrequesting/offer_overview.html'), name = 'offer-home'),
    path('request_spot',views.register_spot,name='request-spot'),
    path('offer_spot',views.offer_spot,name='offer-spot'),
    path('offers_filtered',views.OfferFiltered,name = 'offer-filtered'),
    #path('test_forming',views.OfferFiltered,name = 'offer-filtered'),
    #path('offers_filtered',views.OfferFilteredUpdateView.as_view(template_name = 'spotreuesting/offers_filtered'),name = 'offer-filtered'),
    path('spot/<int:pk>/update',views.SpotUpdateView.as_view(),name = 'spot-update'),
    path('offer/<int:pk>/update',views.OfferUpdateView.as_view(),name = 'offer-update'),
    path('offer/<int:pk>/delete',views.OfferDeleteView.as_view(),name = 'offer-delete'),
    path('login',auth_views.LoginView.as_view(template_name='spotrequesting/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='spotrequesting/logout.html'),name='logout'),
    path('export/csv/', views.export_offers_csv, name='export_offers_csv'),
    path('graph',views.graphing,name='graphing')
    ]


# template_name='spotrequesting/login.html'
# path('request_spot',views.register_spot,name='request-spot')
#  path('request_spot',views.SpotCreateView.as_view(),name='request-spot')


#  path('offer_spot',views.offer_spot,name='offer-spot'),



# path('offer/<int:pk>/create',views.OfferCreateView.as_view(),name='create_spot'),