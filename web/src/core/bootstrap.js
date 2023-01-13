import store from '@/store'
import storage from 'store'
import {
  ADMIN_TOKEN
} from '@/store/constants'

export default function Initializer () {
  // storage.remove('Show-header')
  store.commit('SET_ADMINTOKEN', storage.get(ADMIN_TOKEN))

  // store.dispatch('setLang', storage.get(APP_LANGUAGE, 'zh-CN'))
}
