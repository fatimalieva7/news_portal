from goods.models import News
from django.shortcuts import get_list_or_404, render
from goods.utils import q_search
from django.db.models import Q


def news_list(request, category_slug=None):
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', '-created_at')  # Сортировка по дате по умолчанию
    query = request.GET.get('q', None)  # Поиск по заголовку/содержанию

    # Получаем новости в зависимости от категории
    if category_slug == 'all' or not category_slug:
        news = News.objects.all()
    elif query:
        news = News.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        category = get_object_or_404(Categories, slug=category_slug)
        news = News.objects.filter(category=category)

    # Применяем сортировку
    if order_by and order_by != 'default':
        goods  = news.order_by(order_by)

    context = {
        'title': 'Новости',
        'news': current_page,
        'current_category': category_slug,
        'categories': Category.objects.all(),  # Все категории для меню
    }
    return render(request, 'goods/catalog.html', context)