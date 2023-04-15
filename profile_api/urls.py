from django.contrib import admin
from django.urls import path, include
from profile_api.views import HelloWorldApiView, UserProfileViewSet,UserLoginApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', UserProfileViewSet)


urlpatterns = [
    path('hello', HelloWorldApiView.as_view()),
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls))
]
