from ..models import Book, BorrowHistory
from django.db.models import QuerySet
from ..exceptions import BookNotFound,BookHasNoBorrowHistory


def get_all_books():
    return Book.objects.all()

def get_books_by_id(book_id:int)->Book:
    try:
        return Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise BookNotFound(f"ID{Book.id}에 해당하는 책이 없습니다.")
def get_book_borrow_history_for_book(book:Book):
    histories = book.book_history.order_by('borrowed_at')
    if not histories.exists():
        raise BookHasNoBorrowHistory(f"'{book.title}'에 해당하는 대여 기록이 없습니다.")
    return histories

def get_books_by_author(author):
    book = Book.objects.filter(author=author)
    return book

def get_books_by_title_keyword(cls, keyword ):
    book = Book.objects.filter(title__icontains=keyword)
    return book



def get_books_orderd_by_title(title):
    book = Book.objects.all().order_by(title)
    return book
