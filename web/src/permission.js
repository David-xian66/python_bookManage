import router from './router'
import store from './store'
import storage from 'store'
import { ACCESS_TOKEN } from '@/store/constants'

const allowList = ['login', '403', '404'] // 路由权限白名单
const loginRoutePath = '/login' // 重定向登录地址

router.beforeEach((to, from, next) => {
  console.log(to, from)
  /* has token */
  if (storage.get(ACCESS_TOKEN)) {
    if (to.path === loginRoutePath) {
      next({ path: '/' })
    } else {
      next()
    }
  } else {
    if (allowList.includes(to.name)) {
      // 在免登录名单，直接进入
      next()
    } else {
      next({ path: loginRoutePath, query: { redirect: to.fullPath } })
    }
  }
})
//
// router.afterEach(() => {
//   NProgress.done() // finish progress bar
// })
