# Create your views here.
import datetime

from django.db import connection
from django.db.migrations import serializer
from django.db.models import Count
from rest_framework.decorators import api_view

from myapp.handler import APIResponse

from myapp.models import Book, Borrow

from myapp.models import Classification, Tag
from myapp.utils import dict_fetchall


@api_view(['GET'])
def count(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
        book_count = Book.objects.all().count()
        borrow_count = Borrow.objects.filter(status='1').count()
        return_count = Borrow.objects.filter(status='2').count()
        overdue_count = Borrow.objects.filter(expect_time__lt=now).count()
        # 统计借阅排名(sql语句)
        sql_str = "select A.book_id, B.title, count(A.book_id) as count from b_borrow A join b_book B on " \
                  "A.book_id=B.id group by A.book_id order by count desc; "
        with connection.cursor() as cursor:
            cursor.execute(sql_str)
            borrow_rank_data = dict_fetchall(cursor)
        # 统计分类比例(sql语句)
        sql_str = "select B.title, count(B.title) as count from b_book A join B_classification B on " \
                  "A.classification_id = B.id group by B.title order by count desc limit 5; "
        with connection.cursor() as cursor:
            cursor.execute(sql_str)
            classification_rank_data = dict_fetchall(cursor)

        data = {
            'book_count': book_count,
            'borrow_count': borrow_count,
            'return_count': return_count,
            'overdue_count': overdue_count,
            'borrow_rank_data': borrow_rank_data,
            'classification_rank_data': classification_rank_data,
        }
        return APIResponse(code=0, msg='查询成功', data=data)
