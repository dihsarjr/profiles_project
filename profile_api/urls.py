from django.contrib import admin
from django.urls import path
from profile_api.views import HelloWorldApiView

urlpatterns = [
   
    path('',HelloWorldApiView.as_view())
]