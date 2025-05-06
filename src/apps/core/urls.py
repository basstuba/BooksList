from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    # path('', views.list_books, name='list_books'),
    # クラスベースビュー（CBV）を使う場合は下記になる
    path('', views.BookListView.as_view(), name='list_books'),
    # path('<str:book_id>', views.detail_book, name='detail_book'),
    # クラスベースビュー（CBV）を使う場合は下記になる
    path('<str:slug>/', views.BookDetailView.as_view(), name='detail_book'),
    path('<str:book_id>/edit', views.edit_book, name='edit_book')
]