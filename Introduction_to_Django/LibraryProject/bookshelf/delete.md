from bookshelf.models import Book

book = Book.objects.get(title="The Promised Truce")
book.delete()

Book.objects.all()

# Output:
# <QuerySet []>
