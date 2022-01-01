from django.http import Http404
from django.shortcuts import render

# Create your views here.
from .models import Book
from django.shortcuts import render
def get_books(request):
    books = Book.objects.all()

    return render(request, "book_list.html", {"books": books})


def book_detail(request, id):
    try:
        book = Book.objects.get(id = id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist, baby")

    return render(request, "book.detail.html", {"book": book})