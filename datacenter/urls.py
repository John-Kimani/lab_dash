from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('register', views.signUp, name='register')
]