# Create your views here.
from django.db.migrations import serializer
from rest_framework.decorators import api_view

from myapp.handler import APIResponse

from myapp.models import Book

from myapp.models import Classification, Tag


@api_view(['GET'])
def count(request):
    if request.method == 'GET':
        book_count = Book.objects.all().count()
        classification_count = Classification.objects.all().count()
        tag_count = Tag.objects.all().count()
        data = {'book_count': book_count, 'classification_count': classification_count, 'tag_count': tag_count}
        return APIResponse(code=0, msg='查询成功', data=data)
