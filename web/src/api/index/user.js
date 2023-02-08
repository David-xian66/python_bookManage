/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  registerApi: '/myapp/index/user/register',
  loginApi: '/myapp/index/user/login',
}

export const registerApi = function (data) {
  return axios({
    url: api.registerApi,
    method: 'post',
    data: data
  })
}

export const loginApi = function (data) {
  return axios({
    url: api.loginApi,
    method: 'post',
    data: data
  })
}
