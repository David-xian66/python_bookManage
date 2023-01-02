<template>

  <div>
    login page
    <a-button type="primary" @click="handleLogin">登录</a-button>
  </div>

</template>

<script>

export default {
  name: 'Login',
  methods: {
    handleLogin () {
      this.$store.dispatch('Login', 'liunanana').then(res => {
        this.$router.push({ path: '/' })
        this.$message.success('登录成功！')
      }).catch(err => {
        this.$message.error('登录失败！')
      })
    }
  }
}
</script>
