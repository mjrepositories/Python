from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter

# creating router for moving as within our API
router = DefaultRouter()
# declaring the name of a router and which view should be used
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')
router.register("profile",views.UserProfileViewSet)
router.register('feed',views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    # we will have all urls declared in our router
    path('',include(router.urls)),
    path('login/',views.UserLoginApiView.as_view())
]