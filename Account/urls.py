from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('index.html',views.index,name="index"),
    path('register', views.register, name="register"),
    path('login',views.login,name="login"),
    path('home.html',views.homepage,name="homepage"),
]
