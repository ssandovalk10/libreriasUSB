from django.db import models
from django.utils import timezone 

class Bookshop(models.Model):
    nit = models.CharField("Nit", max_length=50, primary_key=True)
    name = models.CharField("Razon Social", max_length=200,unique=True)
    address = models.CharField("Direccion", max_length=200, blank=True, null=True)
    contact = models.CharField("Contacto", max_length=200, blank=True, null=True)
    celphone = models.CharField("Número de celular", max_length=25, blank=True, null=True)


    def __str__(self):
        return self.name

    
class Author(models.Model):
    firstname = models.CharField("Nombres", max_length=200)
    lastname = models.CharField("Apellidos", max_length=200)


    def __str__(self):
        return self.firstname + " " + self.lastname


class Book(models.Model):
    title = models.CharField("Titulo", max_length=200)
    authors = models.ManyToManyField("Author")
    created_date = models.DateTimeField("Fecha creación", default=timezone.now)
    published_date = models.DateTimeField("Fecha Publicacion", blank=True, null=True)

    def __str__(self):
        return self.title

    
class Stock(models.Model):
    bookshop = models.ForeignKey('Bookshop', on_delete=models.PROTECT)
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
    stock = models.IntegerField("Existencias", default=0)

    def __str__(self):
        return self.book.title + "(Libreria: " + self.bookshop.name + ")"

