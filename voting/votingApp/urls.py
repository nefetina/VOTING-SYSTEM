from unicodedata import name
from django.urls import path
from django.conf import settings
from . import views

app_name = 'votingApp'

urlpatterns =[ 
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('logout/', views.logoutUser, name='logout'),
    path('newreg1/', views.newreg1, name='newreg1'),
    path('homepage/', views.homepage, name='homepage'),
    path('application/', views.application, name='application'),
    path('result/', views.result, name='result'),
    path('comelec/', views.comelec, name='comelec'),
    path('peoples/', views.peoples, name='peoples'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('voting/', views.voting, name='voting'),
    path('votinga/', views.votinga, name='votinga'),
]