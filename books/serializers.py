from rest_framework import serializers
from .models import Book
 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'author', 'price')