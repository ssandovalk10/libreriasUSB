from django.contrib import admin
from .models import Bookshop, Author, Book, Stock
# Register your models here.


admin.site.register(Bookshop)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Stock)