from django.urls import path
from . import views

urlpatterns = [
    path('book-list', views.book_list, name='book-list'),
    path('book-list', views.book_list, name='book-create'),
    path('book-list', views.book_list, name='book-update'),
    path('book-list', views.book_list, name='book-delete'),
]