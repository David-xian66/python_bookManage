/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  listApi: '/myapp/end/overview/count'
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
