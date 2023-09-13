from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("number", "title", "subtitle", "authors", "publisher", "published_date", "category", "distrubution_expense")

admin.site.register(Book, BookAdmin)    