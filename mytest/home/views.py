from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Book


def index(request):
    return HttpResponse("You're looking at index")


class BookList(ListView):
    model = Book
    template_name = 'templates/book_list.html'
    queryset = Book.objects.all()
