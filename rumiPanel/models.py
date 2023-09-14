from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

class Book(models.Model):

    number = models.CharField(_("number"), max_length=255)
    title = models.CharField(_("title"), max_length=255)
    subtitle = models.CharField(_("subtitle"), max_length=255, null=True,)
    authors = models.TextField(_("authors"), null=True,)
    publisher = models.CharField(_("publisher"), max_length=255, null=True,)
    published_date = models.DateField(_("published date"), null=True,)
    category = models.CharField(_("category"), max_length=255, null=True,)
    distrubution_expense = models.FloatField(_("distribution expense"))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])