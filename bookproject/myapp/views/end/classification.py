# Create your views here.
from rest_framework.decorators import api_view, authentication_classes

from myapp.auth.authentication import AdminTokenAuthtication
from myapp.handler import APIResponse
from myapp.models import Classification
from myapp.permission.permission import isDemoAdminUser
from myapp.serializers import ClassificationSerializer


@api_view(['GET'])
def list_api(request):
    if request.method == 'GET':
        classifications = Classification.objects.all().order_by('-create_time')
        serializer = ClassificationSerializer(classifications, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def create(request):
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    classification = Classification.objects.filter(title=request.data['title'])
    if len(classification) > 0:
        return APIResponse(code=1, msg='该名称已存在')

    serializer = ClassificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='创建成功', data=serializer.data)

    return APIResponse(code=1, msg='创建失败')


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def update(request):
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    try:
        pk = request.GET.get('id', -1)
        classifications = Classification.objects.get(pk=pk)
    except Classification.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')

    serializer = ClassificationSerializer(classifications, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return APIResponse(code=0, msg='更新成功', data=serializer.data)

    return APIResponse(code=1, msg='更新失败')


@api_view(['POST'])
@authentication_classes([AdminTokenAuthtication])
def delete(request):
    if isDemoAdminUser(request):
        return APIResponse(code=1, msg='演示帐号无法操作')

    try:
        ids = request.GET.get('ids')
        ids_arr = ids.split(',')
        Classification.objects.filter(id__in=ids_arr).delete()
    except Classification.DoesNotExist:
        return APIResponse(code=1, msg='对象不存在')
    return APIResponse(code=0, msg='删除成功')
