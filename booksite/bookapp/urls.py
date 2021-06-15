from django.contrib import admin
from django.urls import path
from bookapp import views


app_name = 'bookapp'
urlpatterns = [

    path('index/',views.index,name='index'),
    path('book/<int:book_id>/',views.detail,name='detail'),
    path('add/',views.add_book,name='add_book'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]