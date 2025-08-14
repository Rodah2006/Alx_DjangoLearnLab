from django.db import models
from django.utils import timezone

class Author(models.Model):
    # Stores author's name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    # Book title
    title = models.CharField(max_length=200)
    # Year of publication
    publication_year = models.IntegerField()
    # Link to Author (One author can have many books)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
