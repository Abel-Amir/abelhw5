from django.urls import path
from .views import get_books, book_detail

urlpatterns = [
    path("books/", get_books, name = "book_view"),
    path("book/<int:id>/", book_detail, name ="book_detail_view")
]