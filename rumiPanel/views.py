from typing import Any
from django.db.models.query import QuerySet
from .models import Book
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q

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
    fields = '__all__'
    
class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'pages/book_edit.html'
    fields = '__all__'

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'pages/book_delete.html'
    success_url = reverse_lazy('book_list')

class SearchResultsListView(generic.ListView):
    model = Book
    context_object_name = 'book_items'
    template_name = 'pages/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(authors__icontains=query) | Q(subtitle__icontains=query)
        )

class SearchBoxTemplateView(generic.TemplateView):
    template_name = 'pages/book_search.html'
