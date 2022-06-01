from . import views
from django.urls import path

urlpatterns = [
    path('', views.AgricultureSectorInGDP,  name = 'AgricultureSectorInGDP'),#name of the function you are calling
]