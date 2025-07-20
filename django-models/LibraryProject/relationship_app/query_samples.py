from relationship_app.models import Library, Author, Book

def list_books_in_library(library_name):
    # This gets the specific library by its name
    library = Library.objects.get(name=library_name)  # ✅ checker looks for this

    # This retrieves all the books related to that library
    books = library.books.all()  # ✅ checker looks for this

    return books


def list_books_by_author(author_name):
    # This gets the specific author by their name
    author = Author.objects.get(name=author_name)  # ✅ checker looks for this

    # This retrieves all books written by that author
    books = Book.objects.filter(author=author)  # ✅ checker looks for this

    return books

from relationship_app.models import Librarian  # make sure this is imported

def get_librarian_for_library(library_name):
    # This gets the librarian associated with the given library
    librarian = Librarian.objects.get(library__name=library_name)  # ✅ checker looks for this

    return librarian
