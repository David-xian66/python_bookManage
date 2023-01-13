from myapp.models import User


def isDemoAdminUser(request):
    adminToken = request.META.get("HTTP_ADMINTOKEN")
    users = User.objects.filter(admin_token=adminToken)
    if len(users) > 0:
        user = users[0]
        # 考虑将角色写死
        print(user.role)
    return True
