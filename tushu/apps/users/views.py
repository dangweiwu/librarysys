from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import AllowAny
from django.db.models import Q
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

import json
from datetime import datetime

from .serializers import UserSerializer, BorrowSerializer

from .models import User, Borrow
from books.models import Books

# Create your views here.


class Work(View):
    '''图书借还系统
    '''

    def get(self, request):
        return render(request, 'books/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return render(request, 'books/index.html')
        else:
            return render(request, 'books/login.html', {'error_msg': '密码或者账号错误'})
def phone(request):
    return render(request,'phone/index.html')


class UserViewSet(APIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        '''查询用户信息
        '''
        key = request.GET.get('key')
        if not key:
            raise serializers.ValidationError('缺少查询参数')
        instance = User.objects.filter(Q(sn=key) | Q(name=key))
        if instance:
            obj = instance[0]
            obj.borrow_num = obj.borrow_set.filter(back_time=None).count()

            serializer = UserSerializer(obj)
            return Response(serializer.data)
        else:
            return Response(UserSerializer().data)

    def post(self, request):
        # 修改用户昵称和密码
        data = request.body.decode('utf-8')
        data = json.loads(data)
        username = data.get('username')
        password = data.get('password')
        print(password)
        if username:
            print(username)
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError('该昵称已存在')
            request.user.username = username

        if password:
            request.user.password = password

        request.user.save()
        return Response('修改成功')

        # if password:
        #     # request.password = request.user.set_password(password)
        #     # print(request.password)
        #     request.user.save()

        #     return Response('修改成功')

        # raise serializers.ValidationError('没有修改任何东西')


class BorrowPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    page_query_param = "page"
    max_page_size = 100


class BorrowView(GenericAPIView):
    serializer_class = BorrowSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    pagination_class = BorrowPagination
    # authentication_classes = ()

    def get_queryset(self):
        user_sn = self.request.GET.get('user_sn')
        print(user_sn)
        if user_sn:
            # 根据学号查询
            tag = self.request.GET.get('tag')
            user = User.objects.filter(sn=user_sn)
            if user.count() == 0:
                raise serializers.ValidationError('学号不存在')
                return None
            else:
                if tag == 'all':
                    return user[0].borrow_set.all()
                else:
                    return user[0].borrow_set.filter(back_time=None)
        else:
            
            # 根据token查询
            return self.request.user.borrow_set.all()

    def get(self, request):

        # user_sn = self.request.GET.get('user_sn')
        # user = User.objects.filter(sn=user_sn)
        queryset = self.get_queryset()

        if queryset is None:
            queryset = []
            # raise serializers.ValidationError('学号不存在')

        # queryset = Borrow.objects.filter(user_id=user[0].id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class Circulate(APIView):
    '''
    借书 还书接口

    tag: borrow or back

    user_sn:用户sn

    books_sn：list类型 书籍sn

    '''
    # authentication_classes = (SessionAuthentication,)
    # permission_classes = (AllowAny,)
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        data = request.body.decode('utf-8')
        data = json.loads(data)
        tag = data.get('tag')
        sn = data.get('user_sn')
        try:
            user = User.objects.get(sn=sn)
        except User.DoesNotExist:
            raise serializers.ValidationError('学号不存在')

        if tag == 'borrow':
            borrows = Borrow.objects.filter(user=user, back_time=None)
            if borrows.count() >= 3:
                raise serializers.ValidationError('您有%s本书未还,已达借书上线。' % 3)

            books_sn = data.get('book_sn')

            if not books_sn:
                raise serializers.ValidationError('你未借任何书！')
            if len(set(books_sn)) != len(books_sn):
                raise serializers.ValidationError('重复借书！')

            if borrows.count() + len(books_sn) > 3:
                raise serializers.ValidationError('借书数量超过可借数量')

            books = Books.objects.filter(sn__in=books_sn)
            for i in books:
                b = Borrow(user=user, books=i)
                b.status = 'out'
                b.save()
            return Response({'num': len(books)})

        if tag == 'back':
            book_sn = data.get('book_sn')
            try:
                book = Books.objects.get(sn=book_sn)
            except Books.DoesNotExist:
                raise serializers.ValidationError('%s该书不存在' % book_sn)

            try:
                borrow = Borrow.objects.get(user=user, books=book, back_time=None)
            except Borrow.DoesNotExist:
                raise serializers.ValidationError('未查询到借书记录')
            else:
                borrow.back_time = datetime.now()
                borrow.status = 'in'
                borrow.save()
                return Response('还书成功')
