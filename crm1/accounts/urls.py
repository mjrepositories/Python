from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    # we gave a name to each path so that Django now knows to which url it should refer to
    path('', views.home,name = 'home'),
    path('user/',views.userPage,name='user_page'),
    path('account/',views.accountSettings,name='account'),
    # brackets below after customer is a django way of making the url dynamic
    # and can very depending on the value in view where we have models information
    path('customer/<str:pk_test>/',views.customer,name='customer'),
    path('products',views.product,name = 'products'),
    path('create_order/<str:pk>/',views.createOrder,name='create_order'),
    path('update_order/<str:pk>/',views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>/',views.deleteOrder,name='delete_order'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name ='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_complete')
]