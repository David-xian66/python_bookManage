import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const constantRouterMap = [
  {
    path: '/portal',
    name: 'portal',
    component: () => import('@/views/index/portal')
  },
  {
    path: '/detail',
    name: 'detail',
    component: () => import('@/views/index/detail')
  },
  {
    path: '/list',
    name: 'list',
    component: () => import('@/views/index/list')
  },
  {
    path: '/',
    redirect: '/admin'
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/admin/login')
  },
  {
    path: '/403',
    name: '403',
    component: () => import('@/views/exception/403')
  },
  {
    path: '/404',
    name: '404',
    component: () => import('@/views/exception/404')
  },
  {
    path: '/500',
    name: '500',
    component: () => import('@/views/exception/500')
  },
  {
    path: '/admin',
    name: 'admin',
    redirect: '/admin/overview',
    component: () => import('@/layout/basicLayout'),
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
      }
    ]
  }
]

export default new Router({
  routes: constantRouterMap
})
