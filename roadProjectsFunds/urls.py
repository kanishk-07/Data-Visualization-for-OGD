from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.roadProjectsFunds,  name = 'roadProjectsFunds'),#name of the function you are calling
]