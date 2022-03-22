from unicodedata import name
from django.urls import path
from django.conf import settings
from . import views

app_name = 'votingApp'

urlpatterns =[ 
    path('', views.index, name='index'),
    path('newreg1/', views.newreg1, name='newreg1'),
    path('new/', views.new, name='new'),
    path('homepage/', views.homepage, name='homepage'),
    path('application/', views.application, name='application'),
    path('result/', views.result, name='result'),
    path('comelec/', views.comelec, name='comelec'),
    path('peoples/', views.peoples, name='peoples'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('comeleclog/', views.comeleclog, name='comeleclog'),
    path('regcomelec/', views.regcomelec, name='regcomelec'),
    path('regcom/', views.regcom, name='regcom'),
    path('comlog/', views.comlog, name='comlog'),
    path('voting/', views.voting, name='voting'),
    path('voting1/', views.voting1, name='voting1'),
]