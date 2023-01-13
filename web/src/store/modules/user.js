import storage from 'store'
import { adminLogin } from '@/api/admin/user'
import { ADMIN_TOKEN } from '@/store/constants'

const user = {
  namespaced: false,
  state: {
    token: '',
    adminToken: ''
  },
  getters: {
    token: state => state.token,
    adminToken: state => state.adminToken
  },
  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
    },
    SET_ADMINTOKEN: (state, adminToken) => {
      state.adminToken = adminToken
    }
  },

  actions: {
    // 管理员登录
    AdminLogin ({commit}, {username, password}) {
      return new Promise((resolve, reject) => {
        adminLogin({
          username,
          password
        }).then(response => {
          const result = response.data
          commit('SET_ADMINTOKEN', result.admin_token)
          storage.set(ADMIN_TOKEN, result.admin_token, 7 * 24 * 60 * 60 * 1000)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    // 管理员退出
    AdminLogout ({ commit, state }) {
      return new Promise((resolve) => {
        commit('SET_ADMINTOKEN', '')
        storage.remove(ADMIN_TOKEN)
        // window.location.reload()
        resolve()
      })
    }
  }
}

export default user
