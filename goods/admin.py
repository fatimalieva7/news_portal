from django.contrib import admin
from goods.models import Categories,News



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }

@admin.register(News)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
