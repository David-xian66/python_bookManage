/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  listApi: '/api/admin/borrow/list',
  createApi: '/api/admin/borrow/create',
  returnBookApi: '/api/admin/borrow/return_book',
  deleteApi: '/api/admin/borrow/delete',
  updateApi: '/api/admin/borrow/update',
  delayApi: '/api/admin/borrow/delay'
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
/**
 * 还书
 */
export const returnBookApi = function (params, data) {
  return axios({
    url: api.returnBookApi,
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data;charset=utf-8'
    },
    params: params,
    data: data
  })
}
/**
 * 延期
 */
export const delayApi = function (params, data) {
  return axios({
    url: api.delayApi,
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data;charset=utf-8'
    },
    params: params,
    data: data
  })
}
