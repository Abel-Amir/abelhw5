from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from .forms import BookForm, CommentForm
from .models import Book, Comment
from django.shortcuts import render
def get_books(request):
    books = Book.objects.all()

    return render(request, "book_list.html", {'books': books})

class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = "book_list.html"
    context_object_name = "books"


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

class BookDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.kwargs['pk']
        comments = Comment.objects.filter(book_id=book_id)
        context['comments'] = comments
        context['comment_form'] = CommentForm


        return context

    def post(self,request, *args, **kwargs):
        print("Hellow world")

        print('here ja;sdfjlasdkjf')
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().context_object_name(**kwargs)
        print('not here')
        if form.is_valid():
            Comment.objects.create(book_id=id, comment_text=form.data.get('comment_text'))
        else:
            form = CommentForm()
        context['comment_form'] = form



        return self.render_to_response(context=context)

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

class BookCreateView(CreateView):
    model = Book
    template_name = 'add_book.html'
    form_class = BookForm
    success_url = '/books/'