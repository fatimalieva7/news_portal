from django.shortcuts import render
from .models import Category, News
from django.shortcuts import get_object_or_404



def index(request):
    context = {
        'categories': Category.objects.all(),
        'news': News.objects.all(),
    }
    return render(request, 'main/index.html', context)
def latest_news(request):
    context = {
        'categories': Category.objects.all(),
        'news': News.objects.all(),
    }
    return render(request, 'main/latest_news.html', context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    news_list = News.objects.filter(category=category)
    context = {
        'categories': categories,
        'news': news_list,  
        'category': category,
    }
    return render(request, 'main/category.html', context)

def blog_details(request):
    context = {
        'categories': Category.objects.all(),
        'news': News.objects.all(),
    }
    

    return render(request, 'main/blog_details.html', context)
