from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book  # ✅ required import

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view for displaying a specific library’s details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ required
    context_object_name = 'library'  # ✅ required
