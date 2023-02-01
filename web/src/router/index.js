import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const constantRouterMap = [
  // ************* 前台路由 **************
  {
    path: '/index',
    name: 'index',
    redirect: '/index/portal',
    component: () => import('@/layout/index/indexLayout'),
    children: [
      {
        path: 'portal',
        name: 'portal',
        component: () => import('@/views/index/portal')
      },
      {
        path: 'detail',
        name: 'detail',
        component: () => import('@/views/index/detail')
      },
      {
        path: 'list',
        name: 'list',
        component: () => import('@/views/index/list')
      },
      {
        path: 'contentLeft',
        name: 'contentLeft',
        component: () => import('@/views/index/content-left')
      },
      {
        path: 'header',
        name: 'header',
        component: () => import('@/components/index/header')
      },
      {
        path: 'footer',
        name: 'footer',
        component: () => import('@/components/index/footer')
      },
      {
        path: 'contentRight',
        name: 'contentRight',
        component: () => import('@/views/index/content-right')
      }
    ]
  },
  // ************* 后台路由 **************
  {
    path: '/admin',
    name: 'admin',
    redirect: '/admin/overview',
    component: () => import('@/layout/admin/adminLayout'),
    children: [
      {
        path: 'overview',
        name: 'overview',
        component: () => import('@/views/admin/overview')
      },
      {
        path: 'book',
        name: 'book',
        component: () => import('@/views/admin/book')
      },
      {
        path: 'classification',
        name: 'classification',
        component: () => import('@/views/admin/classification')
      },
      {
        path: 'tag',
        name: 'tag',
        component: () => import('@/views/admin/tag')
      },
      {
        path: 'loginLog',
        name: 'loginLog',
        component: () => import('@/views/admin/login-log')
      },
      {
        path: 'opLog',
        name: 'opLog',
        component: () => import('@/views/admin/op-log')
      },
      {
        path: 'errorLog',
        name: 'errorLog',
        component: () => import('@/views/admin/error-log')
      },
      {
        path: 'banner',
        name: 'banner',
        component: () => import('@/views/admin/banner')
      },
      {
        path: 'ad',
        name: 'ad',
        component: () => import('@/views/admin/ad')
      },
      {
        path: 'notice',
        name: 'notice',
        component: () => import('@/views/admin/notice')
      },
      {
        path: 'comment',
        name: 'comment',
        component: () => import('@/views/admin/comment')
      },
      {
        path: 'borrow',
        name: 'borrow',
        component: () => import('@/views/admin/borrow')
      },
      {
        path: 'user',
        name: 'user',
        component: () => import('@/views/admin/user')
      },
      {
        path: 'sysInfo',
        name: 'sysInfo',
        component: () => import('@/views/admin/sys-info')
      }
    ]
  },
  {
    path: '/admin-login',
    name: 'admin-login',
    component: () => import('@/views/admin/admin-login')
  }
]

export default new Router({
  routes: constantRouterMap
})
