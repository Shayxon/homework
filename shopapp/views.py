from django.shortcuts import render
from .models import Product, Video

def product_list(request):
    products = Product.objects.all()
    videos = Video.objects.all()
    return render(request, 'products.html', {'products': products, 'videos': videos})