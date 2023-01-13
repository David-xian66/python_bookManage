/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  adminLogin: '/myapp/adminLogin',
  listApi: '/myapp/user/list',
  createApi: '/myapp/user/create',
  deleteApi: '/myapp/user/delete',
  updateApi: '/myapp/user/update'
}

/**
 * 管理员登录
 */
export const adminLogin = function (data) {
  return axios({
    url: api.adminLogin,
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data;charset=utf-8'
    },
    data: data
  })
}

/**
 * 列表
 */
export const listApi = function (data) {
  return axios({
    url: api.listApi,
    method: 'get',
    params: data
  })
}

/**
 * 新建
 */
export const createApi = function (data) {
  return axios({
    url: api.createApi,
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data;charset=utf-8'
    },
    data: data
  })
}

/**
 * 删除
 */
export const deleteApi = function (params) {
  return axios({
    url: api.deleteApi,
    method: 'post',
    params: params
  })
}
/**
 * 更新
 */
export const updateApi = function (params, data) {
  return axios({
    url: api.updateApi,
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data;charset=utf-8'
    },
    params: params,
    data: data
  })
}
