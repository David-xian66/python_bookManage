/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  listApi: '/myapp/index/book/list',
  detailApi: '/myapp/index/book/detail',
  addWishUserApi: '/myapp/index/book/addWishUser',
  removeWishUserApi: '/myapp/index/book/removeWishUser',
  getWishBookListApi: '/myapp/index/book/getWishBookList',
  increaseRecommendCountApi: '/myapp/index/book/increaseRecommendCount',
}

/**
 * list
 */
export const listApi = function (data) {
  return axios({
    url: api.listApi,
    method: 'get',
    params: data
  })
}
/**
 * detail
 */
export const detailApi = function (data) {
  return axios({
    url: api.detailApi,
    method: 'get',
    params: data
  })
}

export const addWishUserApi = function (data) {
  return axios({
    url: api.addWishUserApi,
    method: 'post',
    params: data
  })
}

export const removeWishUserApi = function (data) {
  return axios({
    url: api.removeWishUserApi,
    method: 'post',
    params: data
  })
}

export const getWishBookListApi = function (params) {
  return axios({
    url: api.getWishBookListApi,
    method: 'get',
    params: params
  })
}

export const increaseRecommendCountApi = function (data) {
  return axios({
    url: api.increaseRecommendCountApi,
    method: 'post',
    params: data
  })
}
