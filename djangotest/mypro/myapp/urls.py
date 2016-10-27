# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 14:13:54 2016

@author: ak66h_000
"""

from django.conf.urls import url

from . import views
app_name = 'dj'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]