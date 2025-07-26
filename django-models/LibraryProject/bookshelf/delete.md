from bookshelf.models import Book

<<<<<<< HEAD
book = Book.objects.get(title="The Promised Truce")
book.delete()

Book.objects.all()

# Output:
# <QuerySet []>
=======
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Output: Book deleted successfully

# Confirm deletion
Book.objects.all()

# Output: <QuerySet []>
>>>>>>> 5cf1b92 (Add retrieve, update, and delete markdowns for checker)
