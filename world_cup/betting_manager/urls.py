from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home_view, name = 'home-page'),
    path('register',views.register,name = 'register'),
    path('login',auth_views.LoginView.as_view(template_name='betting_manager/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='betting_manager/logout.html'),name='logout'),
    path('about',views.about,name = 'about'),
    path('results',views.results,name = 'results'),
    # with button click value for slug is passed and lands in page url
    path('groups/<slug:group_value>',views.groups,name='groups'),
    #same here -  with button click values for slug are passed and land in page url
    path('betting/<slug:stage>/<slug:match>', views.betting, name='betting'),
    path('sweet_16',views.sweetsixteen,name = 'sweet_16'),
    path('elite_8',views.eliteeight,name = 'elite_8'),
    path('final_4',views.finalfour,name = 'final_4'),
    path('championship',views.championship,name = 'championship'),
    path('not_allowed',views.not_allowed,name = 'not_allowed'),
    path('stage_warning',views.stage_warning,name = 'stage_warning'),
    path('create_matches', views.create_matches, name = 'create_matches')
    # below is the standard way of adding static files for app
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)