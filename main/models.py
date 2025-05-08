from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, default='')
    slug = models.SlugField(unique=True, blank=True, default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class News(models.Model):
    slug = models.SlugField(max_length=30, blank=True, null=True, verbose_name='URL')
    name  = models.CharField(max_length=200, verbose_name='Заголовок',blank=True, null=True)
    description = models.TextField(max_length=1500, verbose_name='Описание',blank=True, null=True)
    image = models.ImageField(upload_to='news_images/', default='default.jpg')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', blank=True, null=True)

