from . import views
from django.urls import path

urlpatterns = [
    path('', views.crimeandliteracy,  name = 'crimeandliteracy'),#name of the function you are calling
]