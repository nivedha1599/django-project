# from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^s/$', views.search, name='search'),
    path('addcart', views.addcart, name='addcart'),
    url(r'checkout', views.checkout, name='checkout'),
    url(r'homepage', views.home, name='home-page'),
    path('videosearch/', views.vdopage, name='videosearch'),
    url(r'vdocart/$', views.vdocart, name='vdocart'),
    path('filesearch/', views.filepage, name='filesearch'),
    url(r'filecart/$', views.filecart, name='filecart'),
 #   url(r'common', views.common_op, name='common'),


   
    
]