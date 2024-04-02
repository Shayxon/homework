from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import ItemSerializer
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='POST', request_body=ItemSerializer)
@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data=request.data)
 
    if Book.objects.filter(**request.data).exists():
        raise serializers.ValidationError('already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def view_items(request):
    if request.query_params:
        items = Book.objects.filter(**request.query_params.dict())
    else:
        items = Book.objects.all()
 
    if items:
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['POST'])
def update_items(request, pk):
    item = Book.objects.get(pk=pk)
    data = ItemSerializer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Book, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)