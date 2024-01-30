from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.some_view, name='some_path'),
]