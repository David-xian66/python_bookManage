/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  listApi: '/api/admin/overview/count',
  sysInfoApi: '/api/admin/overview/sysInfo'
}

/**
 * @des 列表
 */
export const listApi = function (params) {
  return axios({
    url: api.listApi,
    method: 'get',
    params: params
  })
}

/**
 * @des 系统信息
 */
export const sysInfoApi = function (params) {
  return axios({
    url: api.sysInfoApi,
    method: 'get',
    params: params
  })
}
