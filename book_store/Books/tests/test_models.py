from django.test import TestCase
from ..models import Book

class BookTest(TestCase):
    
    def setUp(self):
        Book.objects.create(
            name='Lord of the Rings', rating = 10, author = 'J. R. R. Tolkien'
        )
        Book.objects.create(
            name='Frankenstein', rating = 5, author = 'Mary Shelley'
        )
    def test_book_author(self):
        lotr = Book.objects.get(name='Lord of the Rings')
        frnks = Book.objects.get(name='Frankenstein')
        
        self.assertEqual(
            lotr.get_author(), "Lord of the Rings is written by J. R. R. Tolkien."
        )
        self.assertEqual(
            frnks.get_author(), "Frankenstein is written by Mary Shelley."
        )
        self.assertNotEqual(
            frnks.get_author(), "Frankenstein is written by Mary O'Donnel."
        )