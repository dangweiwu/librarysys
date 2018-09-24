# from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import serializers

from .models import Books
from .serializers import BookSerializer
# Create your views here.


class BookPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    page_query_param = "page"
    max_page_size = 100


class BooksView(GenericAPIView):
    '''
    # 查询
    search 用于查找 sn title authors publisher
    '''

    search_fields = ('sn', 'title', 'authors', 'publisher')
    serializer_class = BookSerializer
    queryset = Books.objects.all()
    pagination_class = BookPagination
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    filter_backends = (filters.SearchFilter,)

    def get(self, request):
        key = request.GET.get('search')
        if not key:
            raise serializers.ValidationError('缺少查询参数')

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
