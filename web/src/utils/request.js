import axios from 'axios'
import store from '@/store'
import storage from 'store'
import notification from 'ant-design-vue/es/notification'
import {ADMIN_TOKEN, BASE_URL, TOKEN} from '@/store/constants'

// 创建 axios 实例
const request = axios.create({
  baseURL: BASE_URL,
  timeout: 180000
})

// 异常拦截处理器
const errorHandler = (error) => {
  console.log('error--->' + error)
  if (error.response) {
    const data = error.response.data
    console.log('error--->' + data)
    // 从 localstorage 获取 token
    const adminToken = storage.get(ADMIN_TOKEN)
    if (error.response.status === 403) {
      notification.error({
        message: '禁止访问',
        description: '禁止访问'
      })
    }
    if (error.response.status === 401) {
      notification.error({
        message: '未登录',
        description: '登录验证失败'
      })
      if (adminToken) {
        // todo 此处两种登出如何处理
        store.dispatch('AdminLogout').then(() => {
          setTimeout(() => {
            window.location.reload()
          }, 500)
        })
      }
    }
  }
  return Promise.reject(error)
}

// request interceptor
request.interceptors.request.use(config => {
  const adminToken = storage.get(ADMIN_TOKEN)
  const token = storage.get(TOKEN)

  config.headers['Access-Control-Allow-Headers'] = 'adminToken, token,Content-Type'

  // config.headers['Authorization'] = ''
  config.headers['ADMINTOKEN'] = adminToken
  config.headers['TOKEN'] = token
  return config
}, errorHandler)

// response interceptor
request.interceptors.response.use((response) => {
  if (response.data.code !== 200 && response.data.code !== 0) {
    return Promise.reject(response.data)
  } else {
    return response.data
  }
}, errorHandler)

export default request
