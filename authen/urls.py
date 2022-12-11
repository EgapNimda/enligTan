from django.contrib import admin
from django.urls import path
from authen import views


urlpatterns = [
    
    path("/signIn",views.signIn),
    path("/signUp",views.signUp),
]