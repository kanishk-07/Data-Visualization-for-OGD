from . import views
from django.urls import path

urlpatterns = [
    path('', views.budgetAllocationPolice,  name = 'budgetAllocationPolice')#name of the function you are calling
]