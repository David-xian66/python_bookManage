/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  adminLogin: '/api/admin/adminLogin',
  listApi: '/api/admin/user/list',
  createApi: '/api/admin/user/create',
  deleteApi: '/api/admin/user/delete',
  updateApi: '/api/admin/user/update',
  updatePwdApi: '/api/admin/user/updatePwd',
  infoApi: '/api/admin/user/info'
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
 * 基本信息
 */
export const infoApi = function (data) {
  return axios({
    url: api.infoApi,
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
/**
 * 更新密码
 */
export const updatePwdApi = function (params, data) {
  return axios({
    url: api.updatePwdApi,
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data;charset=utf-8'
    },
    params: params,
    data: data
  })
}
