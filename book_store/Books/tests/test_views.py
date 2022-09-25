import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Book
from ..serializers import BookSerializer
from .book_factory import BookFactory

client = Client()

class GetAllBooksTest(TestCase):
    
    def setUp(self):
        self.LOTR = BookFactory()    
        self.Harry = BookFactory(
            name='Harry Potter', rating = 7, author = 'JK Rowling'
        )
    def test_get_all_books(self):
        response = client.get(reverse('get_post_books'))
        
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class GetSingleBooktest(TestCase):
    
    def setUp(self):
        self.LOTR = BookFactory()    
        self.Harry = BookFactory(
            name='Harry Potter', rating = 7, author = 'JK Rowling'
        )
    def test_get_valid_single_book(self):
        response = client.get(
            reverse('get_delete_update_book', kwargs={'pk': self.LOTR.pk})
        )                
        book = Book.objects.get(pk = self.LOTR.pk)
        serializer = BookSerializer(book, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_invalid_single_book(self):
        response = client.get(
            reverse('get_delete_update_book', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
class CreateNewBookTest(TestCase):
    
    def setUp(self):
        self.valid_payload = {
            'name': 'Winnie Pooh',
            'rating': 4.4,
            'author': 'John'
        }
        self.invalid_payload = {
            'name': '',
            'rating': '5',
            'author': 'John'
        }
    def test_create_valid_book(self):
        response = client.post(
            reverse('get_post_books'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_book(self):
        response = client.post(
            reverse('get_post_books'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
class UpdateSingleBookTest(TestCase):

    def setUp(self):
        self.LOTR = BookFactory()    
        self.Harry = BookFactory(
            name='Harry Potter', rating = 7, author = 'JK Rowling'
        )
        self.valid_payload = {
            'name': 'Winnie Pooh',
            'rating': 6,
            'author': 'Sean Connery'
        }
        self.invalid_payload = {
            'name': '',
            'rating': '5',
            'author': 'John'
        }

    def test_valid_update_book(self):
        response = client.put(
            reverse('get_delete_update_book', kwargs={'pk': self.LOTR.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_book(self):
        response = client.put(
            reverse('get_delete_update_book', kwargs={'pk': self.LOTR.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleBookTest(TestCase):

    def setUp(self):
        self.LOTR = BookFactory()    
        self.Harry = BookFactory(
            name='Harry Potter', rating = 7, author = 'JK Rowling'
        )
    def test_valid_delete_book(self):
        response = client.delete(
            reverse('get_delete_update_book', kwargs={'pk': self.LOTR.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_book(self):
        response = client.delete(
            reverse('get_delete_update_book', kwargs={'pk': 301}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
