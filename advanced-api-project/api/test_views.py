from django.test import RequestFactory, TestCase
from rest_framework import status
from api.models import Author, Book
from .views import BookListView, BookCreateView, BookDeleteView, BookDetailView, BookUpdateView
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User


# Create your tests here.
class APITestCase(TestCase):
    def setUp(self):
        # Set up a test user, Author, Book and factory
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.factory = RequestFactory()
        self.author = Author.objects.create(name="Author C") 
        self.book = Book.objects.create(
            title="Old Book", 
            author=self.author, 
            publication_year=2020
        ) 
        self.client.login(username="testuser", password="password123")

    def test_request(self):
        # test to see the list view api works
        request = self.factory.get('/books/')

        view = BookListView.as_view()

        response = view(request)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_create_book(self):
        # test to create a book
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2023
        }

        request = self.factory.post('/books/create/', data, content_type='application/json')

        force_authenticate(request, user=self.user)

        view = BookCreateView.as_view()

        response = view(request)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertIn("New Book", response.data['title']) 


    def test_update_book(self):
        # test to update a book
        data = {
            "title": "Second Book",
            "author": self.author.id,
            "publication_year": 2021
        }
        request = self.factory.put('/books/update/{self.book.id}/', data, content_type='application/json')

        force_authenticate(request, user=self.user)

        view = BookUpdateView.as_view()

        response = view(request, pk=self.book.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # self.assertEqual(response.data['title'],"Second Book")

    def test_detail_book(self):
        # a test to get a books deatil
        request = self.factory.get('/books/update/{self.book.id}/')

        self.client.login(username="testuser", password="password123")

        view = BookDetailView.as_view()

        response = view(request, pk=self.book.id)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data['title'],"Old Book")

    def test_detele_book(self):
        # a test to get a books deatil
        request = self.factory.delete('/books/update/{self.book.id}/')

        force_authenticate(request, user=self.user)

        view = BookDeleteView.as_view()

        response = view(request, pk=self.book.id)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)



