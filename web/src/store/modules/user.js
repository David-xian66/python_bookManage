import storage from 'store'
// import { login, getInfo } from '@/api/login'
import { USER_NAME, ACCESS_TOKEN } from '@/store/constants'

const user = {
  namespaced: false,
  state: {
    token: '',
    name: '',
    sex: ''
  },
  getters: {
    token: state => state.token,
    name: state => state.name,
    sex: state => state.sex
  },
  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
    },
    SET_NAME: (state, name) => {
      state.name = name
    },
    SET_SEX: (state, sex) => {
      state.sex = sex
    }
  },

  actions: {
    Login ({commit}, name) {
      return new Promise((resolve, reject) => {
        commit('SET_NAME', name)
        storage.set(USER_NAME, name)
        storage.set(ACCESS_TOKEN, '19191919191919191919')
        resolve()
      })
    },
    Logout ({ commit, state }) {
      return new Promise((resolve) => {
        commit('SET_TOKEN', '')
        commit('SET_NAME', '')
        commit('SET_SEX', '')
        storage.remove(ACCESS_TOKEN)
        // window.location.reload()
        resolve()
      })
    }
  }
}

export default user
