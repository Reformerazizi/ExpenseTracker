from .models import Book
from django.views import generic
from django.urls import reverse_lazy

class HomepageTemplateView(generic.TemplateView):
    template_name = 'home.html'

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'pages/book_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'pages/book_detail.html'

class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'pages/book_create.html'
    fields = ['number', 'title', 'subtitle', 'authors',
               'publisher', 'published_date', 'category', 'distrubution_expense',]
    
class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'pages/book_edit.html'
    fields = '__all__'

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'pages/book_delete.html'
    success_url = reverse_lazy('book_list')
