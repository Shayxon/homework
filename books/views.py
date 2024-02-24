from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class BookListView(ListView):
    model = Book
    template_name = 'book-list.html'
    context_object_name = 'books'
    ordering = ['title']

class BookDetailView(DetailView):
    model = Book
    template_name = 'book-detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    class_form = BookForm
    template_name = 'book-create.html'
    fields = ['title', 'author', 'price', 'publisher']
    success_url = reverse_lazy('books')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'price', 'publisher']
    template_name = 'update.html'
    success_url = reverse_lazy('books')

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("books")