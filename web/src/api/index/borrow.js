/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  listApi: '/api/index/borrow/list',
  createApi: '/api/index/borrow/create',
  returnBookApi: '/api/index/borrow/return_book',
  delayApi: '/api/index/borrow/delay'
}

/**
 * 列表
 */
export const listApi = function (params) {
  return axios({
    url: api.listApi,
    method: 'get',
    params: params
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
