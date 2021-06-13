from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list':book_list
    }

    return render(request,'bookapp/index.html',context)

def detail(request,book_id):
    book = Book.objects.get(id=book_id)
    return render(request,'bookapp/detail.html',{'book':book})
def add_book(request):
    return render(request,'bookapp/add_book.html')