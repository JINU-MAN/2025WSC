from django.urls import path
from . import views
from .views import SignUpViews

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('ask/', views.ask_question, name='ask_question'),
    path('signup/', SignUpViews.as_view(), name='signup')
]