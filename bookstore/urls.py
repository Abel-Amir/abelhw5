from django.urls import path
from .views import get_books, book_detail, add_book, BookDetailView, BookListView, BookCreateView

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('add-book/', BookCreateView.as_view())
]