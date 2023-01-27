/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  listApi: '/myapp/end/errorLog/list'
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
