from django.db import models
from datetime import datetime
# Create your models here.


class News(models.Model):
    '''新闻公告
    '''
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容')
    add_time = models.DateTimeField('创建日期', default=datetime.now)
    author = models.CharField('作者', max_length=50)

    class Meta():
        verbose_name = "新闻公告"
        verbose_name_plural = verbose_name
        ordering = ['-add_time']

    def __str__(self):
        return self.title
