# Generated by Django 2.1 on 2018-08-31 01:21

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('sn', models.CharField(max_length=50, unique=True, verbose_name='学号')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='姓名')),
                ('department', models.CharField(max_length=50, null=True, verbose_name='系')),
                ('grade', models.CharField(max_length=50, null=True, verbose_name='年级')),
                ('start_date', models.DateField(null=True, verbose_name='入学日期')),
                ('end_date', models.DateField(null=True, verbose_name='毕业日期')),
                ('Professional', models.CharField(max_length=50, null=True, verbose_name='专业')),
                ('birth_day', models.DateField(blank=True, null=True, verbose_name='出生日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女'), ('unknown', '未知')], default='unknow', max_length=10, verbose_name='性别')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='电话')),
                ('address', models.TextField(blank=True, null=True, verbose_name='地址')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='借阅时间')),
                ('books', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Books', verbose_name='书')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='借阅者')),
            ],
        ),
    ]
