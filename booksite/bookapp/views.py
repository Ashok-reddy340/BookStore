from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm


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
    if request.method=="POST":
        name = request.POST.get('name',)
        author = request.POST.get('author',)
        price = request.POST.get('price',)
        book_image = request.FILES['book_image']

        book = Book(name=name,author=author,price=price,book_image=book_image)
        book.save()

    return render(request,'bookapp/add_book.html')
def update(request,id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/index/')
    return render(request,'bookapp/edit.html',{ 'form':form,'book':book})
def delete(request,id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('/index/')
    return render(request,'bookapp/delete.html')