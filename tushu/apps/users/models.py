from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import Books


# Create your models here.


class User(AbstractUser):
    '''
    学生数据库
    '''
    sn = models.CharField('学号', unique=True, max_length=50)
    name = models.CharField('姓名', max_length=50, null=True)
    department = models.CharField('系', max_length=50, null=True)
    classx = models.CharField('班级', max_length=50, null=True)
    start_date = models.DateField('入学日期', null=True)
    end_date = models.DateField('毕业日期', null=True, blank=True)
    Professional = models.CharField('专业', max_length=50, null=True)
    birth_day = models.DateField('出生日', null=True, blank=True)
    gender = models.CharField('性别', max_length=10, choices=(
        ('male', '男'), ('female', '女'), ('unknown', '未知')), default='unknow')
    phone = models.CharField('电话', max_length=20, blank=True, null=True)
    address = models.TextField('地址', blank=True, null=True)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if len(self.password) < 20:
            self.set_password(self.password)

        print(self.password)
        super(User, self).save(*args, **kwargs)


class Borrow(models.Model):
    '''借阅记录
    '''
    user = models.ForeignKey(User, verbose_name='借阅者', on_delete=models.CASCADE, null=True)
    books = models.ForeignKey(Books, verbose_name='书', on_delete=models.SET_NULL, null=True)
    time = models.DateTimeField('借阅时间', auto_now=True, null=True)
    back_time = models.DateTimeField('还书时间', null=True, blank=True)

    class Meta:
        verbose_name = '借阅记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name
