/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  listApi: '/api/index/comment/list',
  listMyCommentsApi: '/api/index/comment/listMyComments',
  createApi: '/api/index/comment/create',
  deleteApi: '/api/index/comment/delete',
  likeApi: '/api/index/comment/like',
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
 * like
 */
export const likeApi = function (params) {
  return axios({
    url: api.likeApi,
    method: 'post',
    params: params
  })
}

/**
 * listMyCommentsApi
 */
export const listMyCommentsApi = function (params) {
  return axios({
    url: api.listMyCommentsApi,
    method: 'get',
    params: params
  })
}
