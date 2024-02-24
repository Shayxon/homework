from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book_create/', views.BookCreateView.as_view(), name='book_create'),
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='update'),  
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='delete'),  
]