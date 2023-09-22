from typing import Any
from .models import Book
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q, Count
from django.shortcuts import render



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

class GetReportTemplateView(generic.TemplateView):
    template_name = 'pages/get_reports.html'


""" class CategoryChartListView(generic.ListView):
    model = Book
    template_name= 'pages/chart_category.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super(CategoryChartListView, self).get_context_data(**kwargs)
        context["dictCategory"] = Book.objects.values('category').annotate(count=Count('category'))
        dictCategory = context["dictCategory"]
        
        report_list_tuples = []
        report_list = []
        report = []
        final_report = []
        i = 0

        for i in range(0, len(dictCategory)-1):
            j = list(dictCategory[i].items())
            report_list_tuples.append(j)

        for i in report_list_tuples:
            for item in i:
                report_list.append(item)

        for i in report_list:
            for item in i:
                report.append(item)
        
        while(i<int((len(report)-1))):
            final_report.append(report[i+1])
            i = i + 2

        context['report'] = final_report
        return context """
    
def category_chart_report(request):

    dictCategory = Book.objects.values('category').annotate(count=Count('category'))

    report_list_tuples = []
    report_list = []
    report = []
    final_report = []
    category_list = []
    count_list = []
    i = 0
    k = 0
    l = 0

    for c1 in range(0, len(dictCategory)-1):
        j = list(dictCategory[c1].items())
        report_list_tuples.append(j)

    for c2 in report_list_tuples:
        for i1 in c2:
            report_list.append(i1)

    for c3 in report_list:
        for i2 in c3:
            report.append(i2)
        
    while( i<(len(report)-1) ):
        final_report.append(report[i+1])
        i = i + 2
    
    while( k<(len(final_report)-1) ):
        category_list.append(final_report[k])
        k = k + 2
    
    while( l<(len(final_report)-1) ):
        count_list.append(final_report[l+1])
        l = l + 2
        
    return render(request, 'pages/chart_category.html', 
                  {"final_report": final_report, "category_list": category_list, "count_list": count_list})


class PublicationReportChartTemplateView(generic.TemplateView):
    template_name = 'pages/chart_publication.html'