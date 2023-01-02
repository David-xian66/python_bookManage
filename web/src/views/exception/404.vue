<template>
  <a-result status="404" title="404" sub-title="抱歉，页面未找到。">
    <template #extra>
      <a-button type="primary" @click="toHome">
        返回首页
      </a-button>
    </template>
  </a-result>
</template>

<script>
export default {
  name: '404',
  methods: {
    toHome () {
      this.$router.push({ path: '/' })
    }
  }
}
</script>
