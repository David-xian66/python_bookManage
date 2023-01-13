from rest_framework import serializers

from myapp.models import Book, Classification, Tag, User, Comment, Record, LoginLog, Borrow, BorrowLog


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = User
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    comment_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    # 额外字段
    title = serializers.ReadOnlyField(source='book.title')
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'comment_time', 'book', 'user', 'title', 'username']


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class LoginLogSerializer(serializers.ModelSerializer):
    log_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = LoginLog
        fields = '__all__'


class BorrowSerializer(serializers.ModelSerializer):
    borrow_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    expect_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    return_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    # extra
    username = serializers.ReadOnlyField(source='user.username')
    title = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = Borrow
        fields = '__all__'


class BorrowLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowLog
        fields = '__all__'
