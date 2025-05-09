from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .exceptions import BookHasNoBorrowHistory, BookNotFound
from .services import book_service

# Create your views here.

def book_list(request):
    books = book_service.get_all_books()
    return render(request,'book/book_list.html',{'books':books})

def book_history(request, book_id):
    try:
        book = book_service.get_books_by_id(book_id)
        history = book_service.get_book_borrow_history_for_book(book)
    except BookNotFound as e:
        return HttpResponseNotFound(str(e))
    except BookHasNoBorrowHistory as e:
        return render(request, 'book/no_history.html',{'message':str(e)})
    return render(request,'book/book_history.html',{'book':book, 'history':history})