from django.urls import path

from . import views
from .views import BookList

urlpatterns = [
    path('index', views.index, name='index'),
    path('buy-book', BookList.as_view(), name='buy_book'),
]