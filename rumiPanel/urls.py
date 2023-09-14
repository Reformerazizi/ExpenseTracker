from django.urls import path
from .views import (
    HomepageTemplateView,
    BookListView,
    BookDetailView,
    BookCreateView,
)

urlpatterns = [
    path('', HomepageTemplateView.as_view(), name='home'),
    path('Books/', BookListView.as_view(), name='book_list'),
    path('Book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('BookCreate/', BookCreateView.as_view(), name='book_create' )
]
