from django.urls import path
from .views import hello_api
from . import views

urlpatterns = [
    path('hello/',hello_api),
    path('post/',views.receive_post, name="post"),

]