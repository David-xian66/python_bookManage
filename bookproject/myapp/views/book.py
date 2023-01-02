# Create your views here.
from rest_framework.decorators import api_view

from myapp.handler import APIResponse
from myapp.models import Classification, Book, Tag
from myapp.serializers import BookSerializer


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        keyword = request.GET.get("keyword", None)
        c = request.GET.get("c", None)
        tag = request.GET.get("tag", None)
        if keyword:
            books = Book.objects.filter(title__contains=keyword).order_by('-create_time')
        elif c:
            classification = Classification.objects.get(pk=c)
            books = classification.classification_book.all()
        elif tag:
            tag = Tag.objects.get(id=tag)
            print(tag)
            books = tag.book_set.all()
        else:
            books = Book.objects.all().order_by('-create_time')

        serializer = BookSerializer(books, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['GET'])
def detail(request):
    try:
        pk = request.GET.get('id', -1)
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
def create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)
    else:
        print(serializer.errors)

    return APIResponse(code=1, msg='创建失败')


@api_view(['POST'])
def update(request):
    try:
        pk = request.GET.get('id', -1)
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='查询成功', data=serializer.data)
    else:
        print(serializer.errors)

    return APIResponse(code=1, msg='更新失败')


@api_view(['POST'])
def delete(request):
    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        Book.objects.filter(id__in=ids_arr).delete()
    except Book.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')
    return APIResponse(code=0, msg='删除成功')
