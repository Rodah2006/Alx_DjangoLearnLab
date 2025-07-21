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
