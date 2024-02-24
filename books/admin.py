from django.contrib import admin
from .models import Book

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'image']