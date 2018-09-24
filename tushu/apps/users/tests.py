# from django.test import TestCase
import requests
import json
# Create your tests here.


data = {
    'user_sn': '20190002',
    # 'books_sn': ['000026', '000023', '000015'],
    'books_sn': ['000026'],

    'tag':'borrow'
}
r = requests.post('http://127.0.0.1:8000/circulate/', data=json.dumps(data, ensure_ascii=False))
print(r.text)


# data = {
#     'user_sn':'20190002',
#     'book_sn':'1122',
#     'tag':'back',
# }
# r = requests.post('http://127.0.0.1:8000/circulate/',data=json.dumps(data,ensure_ascii=False))
# print(r.content)


# data = {
#     'user_sn':'20190002',
#     'book_sn':'000026',
#     'tag':'back',
# }
# r = requests.post('http://127.0.0.1:8000/circulate/',data=json.dumps(data,ensure_ascii=False))
# print(r.content)