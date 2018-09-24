from django.db import models
# 图书


class Books(models.Model):
    '''图书
    '''
    sn = models.CharField('编码', max_length=50, unique=True)
    title = models.CharField('书名', max_length=100, null=True, blank=True)
    authors = models.CharField('作者', max_length=100, null=True, blank=True)
    publisher = models.CharField('出版社', max_length=100, null=True, blank=True)
    publication_date = models.DateField('出版日期', null=True, blank=True)
    status = models.CharField('状态', max_length=5, choices=(('in', '在库'), ('out', '出库')))
    desc = models.TextField('备注', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='分类')

    class Meta:
        verbose_name = "图书"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Category(models.Model):
    '''图书分类
    '''
    name = models.CharField('类名', max_length=50, unique=True)
    room = models.CharField('房间', max_length=50)
    site = models.CharField('书架', max_length=50)

    class Meta:
        verbose_name = "图书分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
