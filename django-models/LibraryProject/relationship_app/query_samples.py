from relationship_app.models import Book, Author, Librarian, Library

# List all books in a library (Example for library with id=1)
books_in_library = Book.objects.filter(library__id=1)
print("Books in Library ID 1:")
for book in books_in_library:
    print(book.title)

# Query all books by a specific author (Example for author with id=1)
books_by_author = Book.objects.filter(author__id=1)
print("\nBooks by Author ID 1:")
for book in books_by_author:
    print(book.title)

# Retrieve the librarian for a library (Example for library with id=1)
try:
    librarian = Librarian.objects.get(library__id=1)
    print("\nLibrarian for Library ID 1:", librarian.name)
except Librarian.DoesNotExist:
    print("\nNo librarian found for Library ID 1.")
