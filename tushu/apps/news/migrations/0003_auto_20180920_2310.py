# Generated by Django 2.1 on 2018-09-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180901_1946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-add_time'], 'verbose_name': '新闻公告', 'verbose_name_plural': '新闻公告'},
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
    ]
