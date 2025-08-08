from django.db import models

# Author model: Stores author details
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's name

    def __str__(self):
        return self.name


# Book model: Stores book details and links to an Author
class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()  # Year published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    # related_name='books' lets us access all books of an author via author.books.all()

    def __str__(self):
        return self.title



# Author model stores an author's name.
# Book model stores the book's title, year, and links each book to an author.
# One author can have many books (one-to-many relationship).
# related_name='books' lets us access an author's books using author.books.all().
