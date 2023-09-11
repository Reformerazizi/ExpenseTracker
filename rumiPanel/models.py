from django.db import models
from django.utils.translation import gettext as _

class book(models.Model):

    bookId = models.CharField(_("id"), max_length=255)
    title = models.CharField(_("title"), max_length=255)
    subtitle = models.CharField(_("subtitle"), max_length=255, blank=True,)
    author = models.CharField(_("author"), max_length=255)
    publisher = models.CharField(_("publisher"), max_length=255)
    published_date = models.DateField(_("published date"), auto_now=True)
    category = models.CharField(_("category"), max_length=255)
    distrubution_expense = models.FloatField(_("distribution expense"))

    def __str__(self):
        return self.title
