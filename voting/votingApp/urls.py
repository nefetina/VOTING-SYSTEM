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
    path('president/', views.president, name='president'),
    path('vicepresident/', views.vicepresident, name='vicepresident'),
    path('secretary/', views.secretary, name='secretary'),
    path('treasurer/', views.treasurer, name='treasurer'),
    path('auditor/', views.auditor, name='auditor'),
    path('senator/', views.senator, name='senator'),
    path('senator1/', views.senator1, name='senator1'),
    path('senator2/', views.senator2, name='senator2'),
    path('senator3/', views.senator3, name='senator3'),
    path('senator4/', views.senator4, name='senator4'),
    path('governor/', views.governor, name='governor'),
    path('governor1/', views.governor1, name='governor1'),
    path('governor2/', views.governor2, name='governor2'),
    path('governor3/', views.governor3, name='governor3'),
    path('governor4/', views.governor4, name='governor4'),
    path('governor5/', views.governor5, name='governor5'),
    path('governor6/', views.governor6, name='governor6'),
    path('governor7/', views.governor7, name='governor7'),
    path('governor8/', views.governor8, name='governor8'),
    path('governor9/', views.governor9, name='governor9'),
]