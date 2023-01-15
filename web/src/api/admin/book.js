/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  listApi: '/myapp/end/book/list',
  createApi: '/myapp/end/book/create',
  deleteApi: '/myapp/end/book/delete',
  updateApi: '/myapp/end/book/update'
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
      'Content-Type': 'application/form-data'
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
      'Content-Type': 'application/form-data'
    },
    params: params,
    data: data
  })
}
