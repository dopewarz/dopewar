from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^game2/', views.game2, name='game2'),
]
