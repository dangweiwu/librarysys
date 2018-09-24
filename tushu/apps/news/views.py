# from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from .models import News
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class NewsPage(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'
    page_query_param = "page"
    max_page_size = 100


class NewsSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = News
        fields = '__all__'


class NewsView(GenericAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    pagination_class = NewsPage
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
