import store from '@/store'
import storage from 'store'
import {
  ADMIN_TOKEN, ADMIN_USERNAME
} from '@/store/constants'

export default function Initializer () {
  // storage.remove('Show-header')
  store.commit('SET_ADMIN_TOKEN', storage.get(ADMIN_TOKEN))
  store.commit('SET_ADMIN_USERNAME', storage.get(ADMIN_USERNAME))

  // store.dispatch('setLang', storage.get(APP_LANGUAGE, 'zh-CN'))
}
