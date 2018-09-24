import xadmin
from books.models import Books, Category


class BooksAdmin():
    list_display = ['sn', 'title', 'authors', 'publisher', 'publication_date', 'status', 'desc', 'category']
    search_fields = ['title', 'authors', 'publisher', 'publication_date', 'status', 'desc', 'category']
    list_filter = ['title', 'authors', 'publisher', 'publication_date', 'status', 'desc', 'category']


class CategoryAdmin():
    list_display = ['name', 'room', 'site']
    search_fields = ['name', 'room', 'site']
    list_filter = ['name', 'room', 'site']


xadmin.site.register(Books, BooksAdmin)
xadmin.site.register(Category, CategoryAdmin)
