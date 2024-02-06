from django.contrib import admin
from .models import Product, Video

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'image']
    list_filter = ['price']
    search_fields = ['name']

@admin.register(Video)
class AdminProduct(admin.ModelAdmin):
    list_display = ['title', 'video']
    search_fields = ['title']    
