from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render
from . import views

urlpatterns = [
    url(r'^$',views.ShowSl ) ,
    url(r'^a',views.ListSlavesView.as_view(),name='list')
    #url(r'^sl', 'slaves.urls') ,
    #url(r'^admin/', admin.site.urls),
]
