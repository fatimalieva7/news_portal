from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog_details', views.blog_details, name='blog_details'),
    path('blog', views.blog, name='blog'),
    path('categori', views.categori, name='categori'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('latest_news', views.latest_news, name='latest_news'),
    path('main', views.main, name='main'),
]