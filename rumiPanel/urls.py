from django.urls import path
from .views import HomepageTemplateView, BookListView

urlpatterns = [
    path('', HomepageTemplateView.as_view(), name='home'),
    path('Books/', BookListView.as_view(), name='book_list')
]
