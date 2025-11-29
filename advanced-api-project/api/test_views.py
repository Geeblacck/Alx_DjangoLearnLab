from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()

        # Create test Author and Book
        self.author = Author.objects.create(name='John Doe')
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2023,
            author=self.author
        )

        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.id})
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book.id})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.id})


    def test_book_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)


    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password')
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='password')
        data = {'title': 'Updated Book'}
        response = self.client.put(self.update_url, {**data, 'publication_year': 2023, 'author': self.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)


    def test_create_book_unauthenticated(self):
        data = {'title': 'Fail Book', 'publication_year': 2023, 'author': self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_unauthenticated(self):
        data = {'title': 'Fail Update'}
        response = self.client.put(self.update_url, {**data, 'publication_year': 2023, 'author': self.author.id})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_filter_by_title(self):
        response = self.client.get(f"{self.list_url}?title=Test Book")
        self.assertEqual(len(response.data), 1)

    def test_search_by_author_name(self):
        response = self.client.get(f"{self.list_url}?search=John Doe")
        self.assertEqual(len(response.data), 1)

    def test_order_by_publication_year(self):
        Book.objects.create(title='Another Book', publication_year=2022, author=self.author)
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.data[0]['publication_year'], 2022)


