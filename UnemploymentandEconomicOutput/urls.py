from . import views
from django.urls import path

urlpatterns = [
    path('', views.UnemploymentandEconomicOutput,  name = 'UnemploymentandEconomicOutput'),#name of the function you are calling
]