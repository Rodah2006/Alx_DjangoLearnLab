
from django.db import models

# One Author can have many Books
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# One Book belongs to one Author, and can have many Reviews
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

# One Review belongs to one Book
class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Review for {self.book.title}"
