from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
     path('', views.homepage, name='homepage.html'),
     path('homepage', views.homepage, name='homepage.html'),
     path('homepage/addblog', views.addblog, name='addblog'),
     path('homepage/seeblogs', views.seeblogs, name='seeblogs'),
     path('homepage/seebyid', views.seebyid, name='seebyid'),
     path('homepage/deletebyid', views.deletebyid, name='deletebyid'),
     path('homepage/update', views.update, name='update'),
     path('homepage/seecomment', views.seecomment, name='seecomment'),
     path('homepage/addcomment', views.addcomment, name='addcomment'),
]

