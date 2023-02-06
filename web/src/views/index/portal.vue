<template>
  <div class="portal">
    <Header />
    <div class="portal-content">
      <div class="portal-content-left">
        <ContentLeft />
      </div>
      <div class="portal-content-right">
        <ContentRight />
      </div>
    </div>
    <Footer />
  </div>
</template>
<script>
import Header from '@/views/index/components/header'
import Footer from '@/views/index/components/footer'
import ContentLeft from '@/views/index/components/content-left'
import ContentRight from '@/views/index/components/content-right'

export default {
  components: {
    Footer,
    Header,
    ContentLeft,
    ContentRight
  },
  data () {
    return {
    }
  }
}
</script>
<style scoped lang="less">

.portal-content {
  display: flex;
  flex-direction: row;
  width: 1100px;
  margin: 80px auto;
  .portal-content-left {
  }
  .portal-content-right{
    flex: 1;
    width: 100%;
    padding-right: 20px;
  }

}
</style>
