import random, string
from django.db import models
from django.utils.text import slugify



class Category(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=50, verbose_name='Название')

    # Автослаг
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class News(models.Model):
    slug = models.SlugField(max_length=30)
    title = models.CharField(max_length=60, verbose_name='Заголовок')
    name = models.CharField(max_length=30, verbose_name='Название')
    content = models.TextField(max_length=1500, verbose_name='Описание')
    image = models.ImageField(upload_to='news_images', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    # Автослаг
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


