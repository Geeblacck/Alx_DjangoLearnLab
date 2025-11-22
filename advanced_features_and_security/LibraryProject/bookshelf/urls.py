from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_books, name='book_list'),
    path('create/', views.create_book, name='create_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
]
