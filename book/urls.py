from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list,name='book_list'),
    path('<int:book_id>/history',views.book_history ,name='book_history'),
]