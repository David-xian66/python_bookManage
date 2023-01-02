import store from '@/store'
import storage from 'store'
import {
  ACCESS_TOKEN,
  USER_NAME
} from '@/store/constants'

export default function Initializer () {
  // storage.remove('Show-header')
  store.commit('SET_TOKEN', storage.get(ACCESS_TOKEN))
  store.commit('SET_NAME', storage.get(USER_NAME))

  // store.dispatch('setLang', storage.get(APP_LANGUAGE, 'zh-CN'))
}
