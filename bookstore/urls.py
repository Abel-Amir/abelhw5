from django.urls import path
from .views import get_books, book_detail, add_book

urlpatterns = [
    path("books/", get_books, name = "book_view"),
    path("books/<int:id>/", book_detail, name ="book_detail_view"),
    path("add-book/", add_book, name = "add_book_view")
]