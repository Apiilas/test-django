from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView
from .models import Book


def index(request):
    return HttpResponse("You're looking at index")


class BookList(ListView):
    model = Book
    template_name = 'book_list.html'
    queryset = Book.objects.all()

    def post(self, request):
        if request.method == 'POST':
            book_id = request.POST.get('book_id')
            book = Book.objects.get(id=book_id)

            return render(request, 'success_buy.html', {'book': book})
        else:
            return redirect('book_list.html')
