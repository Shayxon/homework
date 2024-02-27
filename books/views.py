from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings

class BookListView(View):
    template_name = 'book-list.html'
    
    def get(self, request):
        books = Book.objects.all().order_by('title')
        return render(request, self.template_name, {'books': books})

class BookDetailView(View):
    template_name = 'book-detail.html'
    
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, self.template_name, {'book': book})

class BookCreateView(View):
    template_name = 'book-create.html'
    
    def get(self, request):
        form = BookForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('books'))
        return render(request, self.template_name, {'form': form})

class BookUpdateView(View):
    template_name = 'update.html'
    
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('books'))
        return render(request, self.template_name, {'form': form})

class BookDeleteView(View):
    template_name = 'book-delete.html'
    
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, self.template_name, {'book': book})
    
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect(reverse_lazy('books'))

@require_POST
def contact(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    message += f" my email: {email}"

    send_mail(f"Hi i am {name}!", message, settings.EMAIL_HOST_USER, ['mamajonovibrokhimjon@gmail.com'])
    return redirect('books')