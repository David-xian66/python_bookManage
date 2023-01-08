# Create your views here.
import datetime

from django.db.migrations import serializer
from rest_framework.decorators import api_view

from myapp.handler import APIResponse

from myapp.models import Book, Borrow

from myapp.models import Classification, Tag


@api_view(['GET'])
def count(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
        book_count = Book.objects.all().count()
        borrow_count = Borrow.objects.filter(status='1').count()
        return_count = Borrow.objects.filter(status='2').count()
        overdue_count = Borrow.objects.filter(expect_time__lt=now).count()
        data = {'book_count': book_count,
                'borrow_count': borrow_count,
                'return_count': return_count,
                'overdue_count': overdue_count
                }
        return APIResponse(code=0, msg='查询成功', data=data)
