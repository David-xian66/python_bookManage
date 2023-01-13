<template>
  <div class="header">
    <img class="header-logo" src="@/assets/logo.png" alt="">
    <span class="header-title">图书后台管理</span>
    <div class="empty"></div>
    <span>管理员[{{username}}]</span>
    <a class="header-quit" @click="handleLogout">退出</a>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
      username: ''
    }
  },
  mounted () {
    this.username = this.$store.state.user.name
  },
  methods: {
    handleLogout () {
      this.$store.dispatch('AdminLogout').then(res => {
        this.$router.push({path: '/admin-login'})
      })
    }
  }
}
</script>
<style lang="less" scoped>

.header {
  display: flex;
  flex-direction: row;
  align-items: center; // 垂直居中
  padding-left: 24px;
  padding-right: 24px;

  .header-logo {
    width: 24px;
    height: 24px;
  }

  .header-title {
    margin-left: 24px;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
  }

  .empty {
    flex:1;
  }

  .header-quit {
    margin-left: 12px;
  }
}
</style>
