from django.core.management.base import BaseCommand
from books.models import Article, Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        fairy_tale = "Мцыри"
        books = Book.objects.filter(name__startswith='Классика русской')
        article = Article.objects.filter(name__startswith="Бо")
        article_list = list(article)
        print(article)
        book_to_find = books.filter(articles__in=article_list)
        print(book_to_find)
        # if article:
        #     print(book_to_find.name)
        #
        #     print(f'we have article {article.name} in books')
        # else:
        #     print('Nothing found')
