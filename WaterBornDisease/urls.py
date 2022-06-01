from . import views
from django.urls import path

urlpatterns = [
    path('', views.WaterBornDisease,  name = 'WaterBornDisease'),#name of the function you are calling
]