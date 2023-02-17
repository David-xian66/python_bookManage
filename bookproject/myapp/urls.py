from django.urls import path

from myapp import views

app_name = 'myapp'
urlpatterns = [
    # 后台管理api
    path('admin/overview/count', views.admin.overview.count),
    path('admin/overview/sysInfo', views.admin.overview.sysInfo),
    path('admin/book/list', views.admin.book.list_api),
    path('admin/book/detail', views.admin.book.detail),
    path('admin/book/create', views.admin.book.create),
    path('admin/book/update', views.admin.book.update),
    path('admin/book/delete', views.admin.book.delete),
    path('admin/comment/list', views.admin.comment.list_api),
    path('admin/comment/create', views.admin.comment.create),
    path('admin/comment/update', views.admin.comment.update),
    path('admin/comment/delete', views.admin.comment.delete),
    path('admin/classification/list', views.admin.classification.list_api),
    path('admin/classification/create', views.admin.classification.create),
    path('admin/classification/update', views.admin.classification.update),
    path('admin/classification/delete', views.admin.classification.delete),
    path('admin/tag/list', views.admin.tag.list_api),
    path('admin/tag/create', views.admin.tag.create),
    path('admin/tag/update', views.admin.tag.update),
    path('admin/tag/delete', views.admin.tag.delete),
    path('admin/record/list', views.admin.record.list_api),
    path('admin/record/create', views.admin.record.create),
    path('admin/record/update', views.admin.record.update),
    path('admin/record/delete', views.admin.record.delete),
    path('admin/banner/list', views.admin.banner.list_api),
    path('admin/banner/create', views.admin.banner.create),
    path('admin/banner/update', views.admin.banner.update),
    path('admin/banner/delete', views.admin.banner.delete),
    path('admin/ad/list', views.admin.ad.list_api),
    path('admin/ad/create', views.admin.ad.create),
    path('admin/ad/update', views.admin.ad.update),
    path('admin/ad/delete', views.admin.ad.delete),
    path('admin/notice/list', views.admin.notice.list_api),
    path('admin/notice/create', views.admin.notice.create),
    path('admin/notice/update', views.admin.notice.update),
    path('admin/notice/delete', views.admin.notice.delete),
    path('admin/borrow/list', views.admin.borrow.list_api),
    path('admin/borrow/create', views.admin.borrow.create),
    path('admin/borrow/update', views.admin.borrow.update),
    path('admin/borrow/return_book', views.admin.borrow.return_book),
    path('admin/borrow/delay', views.admin.borrow.delay),
    path('admin/borrow/delete', views.admin.borrow.delete),
    path('admin/loginLog/list', views.admin.loginLog.list_api),
    path('admin/loginLog/create', views.admin.loginLog.create),
    path('admin/loginLog/update', views.admin.loginLog.update),
    path('admin/loginLog/delete', views.admin.loginLog.delete),
    path('admin/opLog/list', views.admin.opLog.list_api),
    path('admin/errorLog/list', views.admin.errorLog.list_api),
    path('admin/user/list', views.admin.user.list_api),
    path('admin/user/create', views.admin.user.create),
    path('admin/user/update', views.admin.user.update),
    path('admin/user/updatePwd', views.admin.user.updatePwd),
    path('admin/user/delete', views.admin.user.delete),
    path('admin/user/info', views.admin.user.info),
    path('admin/adminLogin', views.admin.user.admin_login),

    # 前台管理api
    path('index/classification/list', views.index.classification.list_api),
    path('index/tag/list', views.index.tag.list_api),
    path('index/user/login', views.index.user.login),
    path('index/user/register', views.index.user.register),
    path('index/user/info', views.index.user.info),
    path('index/user/update', views.index.user.update),
    path('index/notice/list_api', views.index.notice.list_api),
    path('index/book/list', views.index.book.list_api),
    path('index/book/detail', views.index.book.detail),
    path('index/book/increaseWishCount', views.index.book.increaseWishCount),
    path('index/book/addWishUser', views.index.book.addWishUser),
    path('index/book/removeWishUser', views.index.book.removeWishUser),
    path('index/book/getWishBookList', views.index.book.getWishBookList),
    path('index/book/increaseRecommendCount', views.index.book.increaseRecommendCount),
    path('index/comment/list', views.index.comment.list_api),
    path('index/comment/listMyComments', views.index.comment.list_my_comment),
    path('index/comment/create', views.index.comment.create),
    path('index/comment/delete', views.index.comment.delete),
    path('index/comment/like', views.index.comment.like),
    path('index/borrow/list', views.index.borrow.list_api),
    path('index/borrow/create', views.index.borrow.create),
    path('index/borrow/return_book', views.index.borrow.return_book),
    path('index/borrow/delay', views.index.borrow.delay),


]
