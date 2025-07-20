from django.shortcuts import render, get_object_or_404
from .models import Library

def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    books = library.books.all()
    return render(request, "relationship_app/library_detail.html", {
        "library": library,
        "books": books
    })
