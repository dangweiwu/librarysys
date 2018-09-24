import xadmin
from news.models import News


class NewsAdmin():
    list_display = ['title', 'add_time', 'author']
    search_fields = ['title', 'add_time', 'author']
    list_filter = ['title', 'content', 'add_time', 'author']


xadmin.site.register(News, NewsAdmin)
