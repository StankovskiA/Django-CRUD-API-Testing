from factory.django import DjangoModelFactory
from Books.models import Book
from faker import Faker

fake = Faker()
class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book    
    
    name = 'Lord of the Rings'
    rating = 5
    author = fake.name()