from . import views
from django.urls import path

urlpatterns = [
    path('', views.yourOwnPlot,  name = 'ownPlot'),#name of the function you are calling
    path('', views.yourOwnPlot,  name = 'yourOwnPlot')
]