<template>
  <a-result status="500" title="500" sub-title="抱歉！服务器异常，请稍后再试，或联系管理员。">
    <template #extra>
      <a-button type="primary" @click="toHome">
        返回首页
      </a-button>
    </template>
  </a-result>
</template>

<script>
export default {
  name: '500',
  methods: {
    toHome () {
      this.$router.push({ path: '/' })
    }
  }
}
</script>
