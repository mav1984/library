from django.contrib import admin
from books.models import Article, Author, Book

admin.site.register(Author)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('articles',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    search_fields = ('name', 'author__name')
