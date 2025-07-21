import os
import sys
import django

# Add the path to your Django project so Python can find it
sys.path.append('/data/data/com.termux/files/home/Alx_DjangoLearnLab/django-models/LibraryProject')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Set up Django
django.setup()

# Import your model
from relationship_app.models import Student

# Sample query - Create a student
student = Student.objects.create(name="Rodah", age=20, email="rodah@example.com")
print("Created student:", student)

# Retrieve and print all students
students = Student.objects.all()
print("All students:")
for s in students:
    print(s.name, s.age, s.email)

from relationship_app.models import Library  # Make sure this is already imported

# Replace "Central Library" with any existing library name in your database
library_name = "Central Library"

try:
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"\nBooks in '{library_name}':")
    for book in books:
        print(f"- {book.title} by {book.author}")
except Library.DoesNotExist:
    print(f"No library found with the name '{library_name}'")

from relationship_app.models import Author, Book  # Ensure these imports are present

# Replace with an actual author name in your database
author_name = "John Doe"

try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"\nBooks by '{author_name}':")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with the name '{author_name}'")

from relationship_app.models import Librarian, Library  # Make sure these imports are present

# Replace with an actual library name that exists in your database
library_name = "Central Library"

try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian for '{library_name}': {librarian.name}")
except Library.DoesNotExist:
    print(f"No library found with the name '{library_name}'")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to '{library_name}'")
