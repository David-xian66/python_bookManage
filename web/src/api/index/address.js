/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  listApi: '/api/index/address/list',
  createApi: '/api/index/address/create',
  deleteApi: '/api/index/address/delete',
  updateApi: '/api/index/address/update'
}

export const listApi = function (data) {
  return axios({
    url: api.listApi,
    method: 'get',
    params: data
  })
}

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

export const deleteApi = function (data) {
  return axios({
    url: api.deleteApi,
    method: 'post',
    params: data
  })
}

export const updateApi = function (params,data) {
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
