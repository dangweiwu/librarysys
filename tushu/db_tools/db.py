import sys
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from books.models import Books, Category
import csv

def create_catefory():
    '''创建图书分类'''
    with open('./data/category.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i in reader:
            print(dict(i))
            obj = Category(**dict(i))
            obj.save()


def create_books():
    '''创建图书'''
    c = Category.objects.get(name='计算机')

    with open('./data/books.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i in reader:
            print(dict(i))
            obj = Books(**dict(i), category=c)
            obj.save()

create_books()
