<template>

  <div>
    业务1..{{ $store.state.user.name }}..{{ $store.getters.name }}
    <a-button type="primary" @click="handleLogout">退出登录</a-button>

    <a-row :gutter="24">
      <a-col :span="8">
        <a-statistic
          title="图书总数"
          :value="data.book_count"
          style="margin-right: 50px"
        />
      </a-col>
      <a-col :span="8">
        <a-statistic
          title="分类总数"
          :value="data.classification_count"
          style="margin-right: 50px"
        />
      </a-col>
      <a-col :span="8">
        <a-statistic
          title="标签总数"
          :value="data.tag_count"
          style="margin-right: 50px"
        />
      </a-col>
    </a-row>
  </div>

</template>

<script>
import {listApi} from '@/api/overview'
import storage from 'store'
import {USER_NAME, ACCESS_TOKEN} from '@/store/constants'

export default {
  name: 'One',
  data () {
    return {
      data: {}
    }
  },
  created () {
    // this.$store.commit('SET_NAME', 'zhangsan')
    // this.$store.dispatch('Login', 'linxiaomei')

    console.log(this.$store.state.user.name)
    console.log(this.$store.getters.name)

    console.log(storage.get(USER_NAME))
    console.log(storage.get(ACCESS_TOKEN))
    this.list()
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
        this.data = res.data
      }).catch(err => {
        this.$message.error(err.data || '获取失败！')
      })
    }
  }
}
</script>
