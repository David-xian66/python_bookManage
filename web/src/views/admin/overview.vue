<template>

  <div>
    业务1..{{ $store.state.user.name }}..{{ $store.getters.name }}
    <a-button type="primary" @click="handleLogout">退出登录</a-button>
  </div>

</template>

<script>
import {listApi} from '@/api/admin'
import storage from 'store'
import {USER_NAME, ACCESS_TOKEN} from '@/store/constants'

export default {
  name: 'One',
  created () {
    // this.$store.commit('SET_NAME', 'zhangsan')
    // this.$store.dispatch('Login', 'linxiaomei')

    console.log(this.$store.state.user.name)
    console.log(this.$store.getters.name)

    console.log(storage.get(USER_NAME))
    console.log(storage.get(ACCESS_TOKEN))
  },
  methods: {
    handleLogout () {
      this.$store.dispatch('Logout').then(res => {
        this.$router.push({ name: 'login' })
      })
    },
    list () {
      listApi({}).then(res => {
        console.log(res.data)
      }).catch(err => {
        this.$message.error(err.data || '获取失败！')
      })
    }
  }
}
</script>
