from django.shortcuts import render
from django.views.generic import(
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .models import News
from .forms import NewsForm


# Список новостей
class NewsListView(ListView):
    model = News
    template_name = 'news_app/news.html'
    context_object_name = 'news'


# Конкретная новость
class NewsDetailView(DetailView):
    model = News
    template_name = 'news_app/new.html'
    context_object_name = 'new'


# Создание Новости
class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news_app/news_create.html'


# Обновление Новости
class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news_app/news_update.html'


# Удаление Новости
class NewsDeleteView(DeleteView):
    model = News
    context_object_name = 'new'
    template_name = 'news_app/news_delete.html'


