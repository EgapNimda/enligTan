
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('account/', views.account),
    path('account/signin', views.signin),
    path('account/signup', views.signup),
]
