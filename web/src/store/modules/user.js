import storage from 'store'
import { adminLogin } from '@/api/admin/user'
import {ADMIN_TOKEN, ADMIN_USERNAME, TOKEN, USERNAME} from '@/store/constants'

const user = {
  namespaced: false,
  state: {
    /** 前台字段 **/
    token: '',
    username: '',

    /** 后台字段**/
    adminToken: '',
    adminUserName: ''
  },
  getters: {
    token: state => state.token,
    username: state => state.username,
    adminToken: state => state.adminToken,
    adminUserName: state => state.adminUserName
  },
  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
    },
    SET_USERNAME: (state, username) => {
      state.username = username
    },
    SET_ADMIN_TOKEN: (state, adminToken) => {
      state.adminToken = adminToken
    },
    SET_ADMIN_USERNAME: (state, adminUserName) => {
      state.adminUserName = adminUserName
    }
  },

  actions: {
    // 后台登录
    AdminLogin ({commit}, {username, password}) {
      return new Promise((resolve, reject) => {
        adminLogin({
          username,
          password
        }).then(response => {
          const result = response.data
          commit('SET_ADMIN_TOKEN', result.admin_token)
          commit('SET_ADMIN_USERNAME', result.username)
          storage.set(ADMIN_TOKEN, result.admin_token)
          storage.set(ADMIN_USERNAME, result.username)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    // 后台退出
    AdminLogout ({ commit, state }) {
      return new Promise((resolve) => {
        commit('SET_ADMIN_TOKEN', '')
        commit('SET_ADMIN_USERNAME', '')
        storage.remove(ADMIN_TOKEN)
        storage.remove(ADMIN_USERNAME)
        resolve()
      })
    },

    // 普通用户登录
    Login ({commit}, {username, password}) {
      // todo
    },
    // 普通用户退出
    Logout ({ commit, state }) {
      return new Promise((resolve) => {
        commit('SET_TOKEN', '')
        commit('SET_USERNAME', '')
        storage.remove(TOKEN)
        storage.remove(USERNAME)
        resolve()
      })
    }
  }
}

export default user
