from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('newreg/', views.newreg, name='newreg'),
    path('homepage/', views.homepage, name='homepage'),
    path('application/', views.application, name='application'),
    path('result/', views.result, name='result'),
    path('comelec/', views.comelec, name='comelec'),
]