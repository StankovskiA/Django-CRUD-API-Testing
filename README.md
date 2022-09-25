# Testing of a Django CRUD Rest API Web Service

In this project I have used the Django Factory and Test modules as well as the Faker module to test the web service.

## 1. The Web Service
The web service is a simple web service with all CRUD functionalities for the model Book which has the attributes book name, rating i author name.

```
Book:
    name: String
    rating: Float
    author: String
```

### API Endpoints
* '/api/books/$' - Method type: GET, POST
    - GET: Returns all books in db
    - POST: Adds new book to db
* '/api/books/<int:pk>/ - Method type: GET, PUT, DELETE
    - GET: Returns a single book with id: pk
    - PUT: Updates the book with id: pk
    - DELETE: Deletes book with id: pk

## 2. Modules
### Factory boy
```
pip install factory_boy
```
Factory Boy is a fixtures replacement for Django tests that provides a convenient, easy and manageable way to create and maintain data needed for tests.
To use factories in my project, I just had to create one file "book_factory.py" in which I created the class BookFactory for the model Book and I set default values for the book model. 
To create objects using the factories I just need to instantiate an object from the class BookFactory. If no parameters for the attributes are passed, the default values of the factory are used to create the model.

```python
# Creating factory class
class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book    
    
    name = 'Lord of the Rings'
    rating = 10.0
    author = 'J.R.R. Tolkien'

# Usage of factories
LOTR = BookFactory() # Uses default values
Harry = BookFactory(
            name='Harry Potter', rating = 7, author = 'JK Rowling'
        ) # Uses custom values
```


## Faker
```
pip install Faker
```
Faker is a Python package that generates fake data of various types such as first names, phone numbers, addresses, barcodes etc. This can be useful during the process of testing because it allows us in a very simple way to test our web service with random data.
To use the Faker module in my factory I decided to get random values for the name of the author by using the name provider of faker.
```python
fake = Faker() # Instantiate Faker object
class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book    
    
    name = 'Lord of the Rings'
    rating = 10.0
    author = fake.name() # Use fake name provider
```
### Django Test

The preferred way to write tests in Django is using the unittest module built-in to the Python standard library, although other modules can be used as well. The Test module provides us with mulitple classes to ease our testing process. 
I have used the class TestCase which offers us functions such as set up with which we can create objects to test our web service with. 

``` python
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

```
Django provides us with an automated way of performing these tests. When I run my tests, the default behavior of the test utility is to find all the test cases (that is, subclasses of unittest.TestCase) in any file whose name begins with test, automatically build a test suite out of those test cases, and run that suite.
