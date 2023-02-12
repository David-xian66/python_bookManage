# Create your views here.
from django.db import connection
from rest_framework.decorators import api_view, authentication_classes

from myapp import utils
from myapp.handler import APIResponse
from myapp.models import Classification, Book, Tag
from myapp.serializers import BookSerializer, ClassificationSerializer
from myapp.utils import dict_fetchall


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        keyword = request.GET.get("keyword", None)
        c = request.GET.get("c", None)
        tag = request.GET.get("tag", None)
        sort = request.GET.get("sort", 'recent')

        # 排序方式
        order = '-create_time'
        if sort == 'recent':
            order = '-create_time'
        elif sort == 'hot' or sort == 'recommend':
            order = '-pv'

        if keyword:
            books = Book.objects.filter(title__contains=keyword).order_by(order)
        elif c and int(c) > -1:
            ids = [c]
            classifications = Classification.objects.filter(pid=c)
            serializer = ClassificationSerializer(classifications, many=True)
            subData = serializer.data
            for item in subData:
                # 添加二级分类的id
                ids.append(item['id'])
            print(ids)

            books = Book.objects.filter(classification_id__in=ids).order_by(order)

        elif tag:
            tag = Tag.objects.get(id=tag)
            print(tag)
            books = tag.book_set.all().order_by(order)
        else:
            books = Book.objects.all().order_by(order)

        serializer = BookSerializer(books, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def detail(request):
    try:
        pk = request.GET.get('id', -1)
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        utils.log_error(request, '对象不存在')
        return APIResponse(code=1, msg='对象不存在')

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)
