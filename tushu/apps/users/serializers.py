from rest_framework import serializers
from users.models import User, Borrow
from books.models import Books


class UserSerializer(serializers.ModelSerializer):
    borrow_num = serializers.IntegerField(default=None)

    class Meta:
        model = User
        fields = ('sn', 'name', 'department', 'classx', 'borrow_num')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('sn', 'title', 'authors', 'publisher')


class BorrowSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True)
    time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    back_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Borrow
        fields = ('books', 'time', 'back_time')
