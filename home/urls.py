from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.indexHome,  name = 'indexHome'),
    #url(r'^$', views.chart, name = 'demo'),
]