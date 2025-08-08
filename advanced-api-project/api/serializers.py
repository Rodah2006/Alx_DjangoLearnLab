from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to prevent future publication years
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['name', 'books']



# BookSerializer serializes all Book fields and checks that the year is not in the future.
# AuthorSerializer serializes an author and their books using nested BookSerializer.
# The 'books' field works because of related_name='books' in the Book model.
