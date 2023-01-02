<template>
  <div class="section weekly-top">
    <div class="hd">
      <h2 class="fw">借阅图书榜</h2>
    </div>
    <div class="bd">

      <ul class="list list-ranking">
        <template v-for="(item, index) in hotBorrowData">
          <li class="item impression_track_chart">
            <span class="rank-num">{{ index + 1 }}.</span>
            <div class="book-info">
              <a class="name" target="_blank">钝感力</a>
              <div class="author">[日] 渡边淳一</div>
            </div>
            <a onclick=""><span class="buy-button">去借阅</span></a>
          </li>
        </template>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HotBorrowCard',
  data() {
    return {
      hotBorrowData: ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    }
  }
}
</script>
<style src="@/style/index/index.less" scoped lang="less"></style>
<style scoped lang="less">
a:link, a:visited, a:focus {
  color: #3377aa;
}
a {
  color: #3377aa;
}
</style>
