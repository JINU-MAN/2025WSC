from enum import auto

from django.db import models
from django.db.models import QuerySet
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title= models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

class BorrowHistory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='book_history')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}-{self.book.title}"


    # @classmethod
    # def get_all_books(cls)->QuerySet['Book']:
    #     return cls.objects.all()
    #
    # @classmethod
    # def get_books_by_author(cls, author) ->QuerySet['Book']:
    #     return cls.objects.filter(author = author)
    # @classmethod
    # def get_books_by_title_keyword(cls, keyword)->QuerySet['Book']:
    #     return cls.objects.filter(title__icontains=keyword)
    #
    # @classmethod
    # def get_books_orderd_by_title(cls)->QuerySet['Book']:
    #     return cls.objects.all().order_by('title')

