from . import views
from django.urls import path

urlpatterns = [
    path('', views.PollutionAndVehicles,  name = 'PollutionAndVehicles'),#name of the function you are calling
]