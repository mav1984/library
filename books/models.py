from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ('name',)


class Article(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} - {self.author.name}'

    class Meta:
        ordering = ('author', 'name')


class Book(models.Model):
    name = models.CharField(max_length=100)
    articles = models.ManyToManyField(Article, related_name='%(class)s_related')

    def __str__(self):
        return self.name