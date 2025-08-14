from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author


class BookAPITestCase(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Author One")
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publication_year=2020
        )

        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.list_url = reverse("book-list")  # Make sure your urls.py names this
        self.detail_url = reverse("book-detail", args=[self.book.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book.id])
        self.delete_url = reverse("book-delete", args=[self.book.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {"title": "Test Book"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Test" in book["title"] for book in response.data))

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2021
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "author": self.author.id,
            "publication_year": 2021
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        data = {
            "title": "Updated Book",
            "author": self.author.id,
            "publication_year": 2022
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
