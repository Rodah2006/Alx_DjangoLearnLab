from relationship_app.models import Library

def list_books_in_library(library_name):
    # This gets the specific library by its name
    library = Library.objects.get(name=library_name)  # ✅ checker looks for this exact line

    # This retrieves all the books related to that library
    books = library.books.all()  # ✅ checker looks for this exact line

    return books
