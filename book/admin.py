from django.contrib import admin

from .apps import BookConfig
# Register your models here.
from .models import Book

admin.site.register(Book)