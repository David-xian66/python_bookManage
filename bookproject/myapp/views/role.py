# Create your views here.
from rest_framework.decorators import api_view

from myapp.handler import APIResponse
from myapp.models import Role
from myapp.serializers import RoleSerializer


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        roles = Role.objects.all().order_by('-create_time')
        serializer = RoleSerializer(roles, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
def create(request):
    roles = Role.objects.filter(title=request.data['title'])
    if len(roles) > 0:
        return APIResponse(code=1, msg='该名称已存在')

    serializer = RoleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)

    return APIResponse(code=1, msg='创建失败')


@api_view(['POST'])
def update(request):
    try:
        pk = request.GET.get('id', -1)
        roles = Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = RoleSerializer(roles, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='更新成功', data=serializer.data)

    return APIResponse(code=1, msg='更新失败')


@api_view(['POST'])
def delete(request):
    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        Role.objects.filter(id__in=ids_arr).delete()
    except Role.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    return APIResponse(code=0, msg='删除成功')
