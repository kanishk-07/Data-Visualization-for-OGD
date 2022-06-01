from . import views
from django.urls import path

urlpatterns = [
    path('', views.literacyRatesStates,  name = 'literacyRatesStates')#name of the function you are calling
]