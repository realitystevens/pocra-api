from django.contrib import admin
from .models import Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'is_published', 'price', 'created_at', 'published_at']
    list_filter = ['is_published', 'created_at', 'published_at']
    search_fields = ['name', 'url', 'description', 'id', 'is_published', 'price', 'created_at', 'published_at']
    ordering = ['name', 'id', 'price', '-created_at', '-published_at']

admin.site.register(Product, ProductAdmin)

admin.site.site_header = 'Pocra Digital Store Administration'

admin.site.site_title = 'Pocra Digital Store'


