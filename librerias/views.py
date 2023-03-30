from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Bookshop

import requests
import json

class LibreriaListView(ListView):
    model = Bookshop


def Search(request):
    if request.method == "POST":
        book_name = request.POST['book_name']
        result = requests.get("https://www.googleapis.com/books/v1/volumes?q="+book_name)
        if (result.status_code ==200):
            contenido = result.json()
            libros = contenido["items"]
            code = json.dumps(libros)
            listBooks = json.loads(code)
            data = []
            print(listBooks)
            for books in listBooks:
                data.append([
                    books['volumeInfo']['title'],
                    books['volumeInfo']['authors'],
                    books['volumeInfo']['publishedDate'],
                    books['volumeInfo']['infoLink'],
                ])
            return render(request, 'librerias/books_list.html', {'books':data})
    return render(request, 'librerias/search.html', {})