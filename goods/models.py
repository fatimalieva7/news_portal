from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=155, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=65, unique=True, verbose_name='URL', null=True, blank=True)


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ('id',)

class News(models.Model):
    slug = models.SlugField(max_length=30, blank=True, null=True, verbose_name='URL')
    name  = models.CharField(max_length=200, verbose_name='Название',blank=True, null=True)
    description = models.TextField(max_length=1500, verbose_name='Описание',blank=True, null=True)
    image = models.ImageField(upload_to='news_images/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория', blank=True, null=True)
    def __str__(self):
        return self.name
        