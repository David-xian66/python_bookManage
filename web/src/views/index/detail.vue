<template>
  <div class="detail">
    <Header />

    <div class="detail-content">
      <div class="detail-content-top">
        <BookInfosView />
      </div>
      <div class="detail-content-bottom">
        <BookContentView />
      </div>
    </div>

    <Footer />
  </div>
</template>
<script>
import Header from '@/views/index/components/header'
import Footer from '@/views/index/components/footer'
import BookInfosView from '@/views/index/components/book-infos-view'
import BookContentView from '@/views/index/components/book-content-view'

export default {
  components: {
    Footer,
    Header,
    BookInfosView,
    BookContentView
  },
  data () {
    return {
    }
  }
}
</script>
<style scoped lang="less">

.detail-content {
  display: flex;
  flex-direction: column;
  width: 1100px;
  margin: 4px auto;
}
</style>
