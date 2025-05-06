from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import generic
from .models import Book


# def list_books(request):
#     books = Book.objects.all()
#     context = {
#         'title': 'List Books',
#         'books': books,
#     }
#     template = loader.get_template('core/list_books.html')
#     return HttpResponse(template.render(context, request))
# これをクラスベースビュー（CBV）で書くと下記になる
class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'core/list_books.html'
    context_object_name = 'books'
    extra_context = {'title': 'List Books'}


# def detail_book(request, book_id):
#     try:
#         book = Book.objects.get(book_id=book_id)
#     except Book.DoesNotExist:
#         book = None

#     context = {
#         'title': 'Detail Book',
#         'book': book,
#     }
#     template = loader.get_template('core/detail_book.html')
#     return HttpResponse(template.render(context, request))
# これをクラスベースビュー（CBV）で書くと下記になる
class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    template_name = 'core/detail_book.html'
    context_object_name = 'book'
    extra_context = {'title': 'Detail Book'}
    slug_field = 'book_id'          # ← パスパラメータに使うフィールド
    slug_url_kwarg = 'slug'            # ←（URLでは str:slug を受け取る）


@login_required
def edit_book_input(request, book_id):
    try:
        book = Book.objects.get(book_id=book_id)
    except Book.DoesNotExist:
        book = None

    context = {
        'title': 'Edit Book(input)',
        'mode': 'input',
        'book': book,
    }
    template = loader.get_template('core/edit_book.html')
    return HttpResponse(template.render(context, request))
# これをクラスベースビュー（CBV）で書くと下記になるが、分岐等が絡むと他の関数を含め全体が複雑になってしまう
# class BookEditInputView(generic.DeleteView):
#     model = Book
#     template_name = 'core/edit_book.html'
#     context_object_name = 'book'
#     extra_context = {
#         'title': 'Edit Book(input)',
#         'mode': 'input',
#     }
#     slug_field = 'book_id'
#     slug_url_kwarg = 'slug'


@login_required
def edit_book_confirm(request, book_id):
    book = Book.objects.get(book_id=book_id)
    book.book_id = request.POST['book_id']
    book.title = request.POST['title']
    book.author = request.POST['author']

    context = {
        'title': 'Edit Book(confirm)',
        'mode': 'confirm',
        'warning_message': 'Are you sure you want to save?',
        'book': book,
    }
    template = loader.get_template('core/edit_book.html')
    return HttpResponse(template.render(context, request))


@login_required
def edit_book_result(request, book_id):
    try:
        book = Book.objects.get(book_id=book_id)
        book.book_id = request.POST['book_id']
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
    except Book.DoesNotExist:
        book = None

    context = {
        'title': 'Edit Book(result)',
        'mode': 'result',
        'success_message': 'Success!',
        'book': book,
    }
    template = loader.get_template('core/edit_book.html')
    return HttpResponse(template.render(context, request))


@login_required
def edit_book(request, book_id):
    if request.method == 'GET':
        return edit_book_input(request, book_id)
    elif request.method == 'POST':
        if request.POST['mode'] == 'input':
            return edit_book_confirm(request, book_id)
        elif request.POST['mode'] == 'confirm':
            return edit_book_result(request, book_id)