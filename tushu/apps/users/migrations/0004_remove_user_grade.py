# Generated by Django 2.1 on 2018-09-01 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180901_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='grade',
        ),
    ]
