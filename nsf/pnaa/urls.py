'''
Created on Dec 22, 2016

@author: kyick
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^arda$', views.map, name='map'),
    
]
