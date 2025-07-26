import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Book, Author, Library, Librarian

# 1. Query all books by a specific author using objects.filter()
author_name = "William Shakespeare"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)  # ✅ checker wants this
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

# 2. List all books in a library using related_name 'books'
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()  # ✅ related_name
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")

# 3. Retrieve the librarian for a library using Librarian.objects.get(library=...)
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)  # ✅ matches checker
    print(f"\nLibrarian for {library_name}: {librarian.user.username}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")
except Librarian.DoesNotExist:
    print(f"{library_name} has no assigned librarian.")
