from django.urls import path
from . import views


app_name = 'news_app'


urlpatterns = [
    path('', views.NewsListView.as_view(), name='news'),
    path('new/<int:pk>', views.NewsDetailView.as_view(), name='new'),
    path('new-create/', views.NewsCreateView.as_view(), name='news_create'),
    path('new-update/<int:pk>', views.NewsUpdateView.as_view(), name='news_update'),
    path('new-delete/<int:pk>', views.NewsDeleteView.as_view(), name='news_delete'),
]
