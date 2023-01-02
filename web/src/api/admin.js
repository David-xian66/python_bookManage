/**
 * api
 */
import axios from '@/utils/request.js'

const api = {
  listApi: 'https://fanyi.baidu.com/pcnewcollection'
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
