from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'




urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('latest-news/', views.latest_news, name='latest_news'),
    path('blog-details/', views.blog_details, name='blog_details')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)