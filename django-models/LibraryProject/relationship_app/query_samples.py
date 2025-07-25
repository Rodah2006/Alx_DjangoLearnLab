# relationship_app/query_samples.py

import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "John Doe"
books = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:")
for book in books:
    print(f"- {book.title}")

# 2. List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in {library_name}:")
    for book in library.books.all():
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"\nLibrary '{library_name}' not found.")

# 3. Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"\nLibrarian of {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"\nNo librarian found for {library_name}.")
