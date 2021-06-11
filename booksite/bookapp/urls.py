from django.contrib import admin
from django.urls import path
from bookapp import views


app_name = 'bookapp'
urlpatterns = [

    path('index/',views.index,name='index'),
    path('book/<int:book_id>/',views.detail,name='detail'),
]