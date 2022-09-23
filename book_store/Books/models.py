from statistics import mode
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    author = models.CharField(max_length=100)
    
    def get_author(self):
        return f'{self.name} is written by {self.author}.'

    def __repr__(self):
        return f'{self.name} is added to store.'