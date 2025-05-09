import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

import pytest
from django.contrib.auth.models import User
from ..models import Book, BorrowHistory
from ..services.book_service import  get_book_borrow_history_for_book,get_books_by_id
from ..exceptions import BookHasNoBorrowHistory,BookNotFound

@pytest.mark.django_db
def test_get_borrow_history_for_book_success():
    #Given
    user = User.objects.create(username='testuser')
    book = Book.objects.create(title='Test Book',author='Tester',isbn='1234567890123')
    BorrowHistory.objects.create(book=book,user=user)
    #When
    histories = get_book_borrow_history_for_book(book)
    #Then
    assert histories.count() ==1
    assert histories.first().user == user

@pytest.mark.django_db
def test_get_borrow_history_for_book_no_history():
    #Given
    book = Book.objects.create(title='Empty Book',author = 'Nobody',
                               isbn='9999999999999')
    #When&Then
    with pytest.raises(BookHasNoBorrowHistory) as exc_info:
        get_book_borrow_history_for_book(book)

    assert '대여 기록이 없습니다' in str(exc_info.value)

@pytest.mark.django_db
def test_get_book_by_id_success():
    book = Book.objects.create(title='Test Book', author='Tester', isbn='1234567890123')
    result = get_books_by_id(book.id)
    assert result == book
    assert result.title == 'Test Book'
@pytest.mark.django_db
def test_get_book_by_id_not_found():
    with pytest.raises(BookNotFound) as exc_info:
        get_books_by_id(9999)
    assert 'ID9999에 해당하는 책이 없습니다' in str(exc_info)