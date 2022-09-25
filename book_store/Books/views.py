from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'rating': float(request.data.get('rating')),
            'author': request.data.get('author')
        }
        
        seriaizer = BookSerializer(data=data)
        if seriaizer.is_valid():
            seriaizer.save()
            return Response(seriaizer.data, status=status.HTTP_201_CREATED)
        return Response(seriaizer.errors, status=status.HTTP_400_BAD_REQUEST)