from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from myapp.models import User


class TokenAuthtication(BaseAuthentication):
    def authenticate(self, request):
        """
        先获取 header 中的token进行解析
        :param request:
        :return:
        """
        adminToken = request.META.get("HTTP_ADMINTOKEN")
        print("检查adminToken==>" + adminToken)
        if not adminToken and User.objects.filter(admin_token=adminToken).count == 0:
            raise exceptions.AuthenticationFailed("验证失败")
        else:
            print('adminToken验证通过')

