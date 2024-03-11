from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "homeapp"
urlpatterns = [

    path('home/', views.home, name="home"),
    path('index/',views.index,name="index"),

]
