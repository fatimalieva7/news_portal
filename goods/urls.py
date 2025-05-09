from django.shortcuts import render
from django.urls import path

from goods import views
app_name = 'goods'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('news/<slug:news_slug>/', views.news, name='news'),
    
]

