import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Book, Author, Library

# 1. Query all books by a specific author
author_name = "William Shakespeare"  # change as needed
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

# 2. List all books in a library
library_name = "Central Library"  # change as needed
try:
    library = Library.objects.get(name=library_name)
    books_in_library = Book.objects.filter(library=library)
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")

# 3. Retrieve the librarian for a library
try:
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # assuming ForeignKey to Librarian model
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")
except AttributeError:
    print(f"{library_name} has no assigned librarian.")
