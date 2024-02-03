from django.shortcuts import render
from .models import *
# Create your views here.

def aboutView(request):
    return render(request=request, template_name='about.html', context={})
    
def contactView(request):
    return render(request=request, template_name='contact.html', context={})

def indexView(request):
    data = AddProductModel.objects.all()
    count = []
    for i in range(1,len(data)+1):
        count.append(i)
    return render(request=request, template_name='index.html', context={'products':data, 'range': count})

def productView(request):
    data = AddProductModel.objects.all()
    return render(request=request, template_name='product.html', context={'products':data})

def testimonialView(request):
    return render(request=request, template_name='testimonial.html', context={})