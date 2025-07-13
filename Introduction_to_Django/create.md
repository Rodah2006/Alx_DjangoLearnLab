from bookshelf.models import Book

# Create and save the Book
book = Book(title="Promised Truce", author="Rodah", publication_year=2013)
book.save()

book

# Output:
# <Book: Promised Truce by Rodah (2013)>
