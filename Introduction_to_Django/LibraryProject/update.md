from bookshelf.models import Book

book = Book.objects.get(title="Promised Truce")
book.title = "The Promised Truce"
book.save()

print(book.title)

# Output:
# The Promised Truce
