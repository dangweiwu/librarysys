from rest_framework import serializers

from books.models import Books, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)

    class Meta:
        model = Books
        fields = '__all__'
