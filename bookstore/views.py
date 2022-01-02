from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import BookForm, CommentForm
from .models import Book, Comment
from django.shortcuts import render
def get_books(request):
    books = Book.objects.all()

    return render(request, "book_list.html", {'books': books})


def book_detail(request, id):
    try:
        book = Book.objects.get(id = id)
        try:
            comments = Comment.objects.filter(book_id = id).order_by('created_date')
        except Comment.DoesNotExist:
            return HttpResponse("No comments")
    except Book.DoesNotExist:
        raise Http404('Book does not exist')
    form = CommentForm(request.POST)
    if form.is_valid():
        Comment.objects.create(book_id=id, comment_text = form.data.get('comment_text'))

    return render(request, 'book_detail.html', {'book': book, 'comments': comments, 'comment_form': form})


def add_book(request):
    method = request.method
    if method == "POST":
        form = BookForm(request.POST, request.FILES)
        print(form.data)
        Book.objects.create(title=form.data['title'],
                            description = form.data['description'],
                            image = request.FILES['image']
                            )
        return redirect('/books/')
    else:
        form = BookForm

    return render(request, 'add_book.html', {'form': form})