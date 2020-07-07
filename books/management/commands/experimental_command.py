from django.core.management.base import BaseCommand
from books.models import Author, Article, Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        fairy_tale = "Война и мир"
        article = Article.objects.filter(name=fairy_tale).first()
        if article:
            for book in Book.objects.all():
                if article in book.articles.all():
                    print(book.name)
