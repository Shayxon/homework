from django.urls import path
from .views import *

urlpatterns = [
    path('', indexView, name='index'),
    path('about/', aboutView, name='about'),
    path('product/', productView, name='product'),
    path('contact/', contactView, name='contact'),
    path('testimonial/', testimonialView, name='testimonial'),
]