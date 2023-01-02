<template>
  <div class="aside">
    <h2>
      <span>图书Top100</span>
      <span class="pl">(随机显示)</span>&nbsp;·&nbsp;·&nbsp;·&nbsp;·&nbsp;·&nbsp;·
      <span class="pl">&nbsp;(<a href="/top250">全部</a>)</span>
    </h2>
    <ul class="entry-list-col3 clearfix">
      <template v-for="item in data">
        <li>
          <p>
            <a href="">
              <img width="67px" src="https://pic.arkread.com/cover/ebook/f/400668268.1657173376.jpg!cover_default.jpg">
            </a>
          </p>
          <h2>
            <a href="" class="title">狂热分子</a>
          </h2>
        </li>
      </template>
    </ul>
  </div>
</template>
<script>
export default {
  name: 'TopCard',
  data() {
    return {
      data: ['1', '1', '1', '1', '1', '1', '1', '1', '1']
    }
  }
}
</script>
<style src="@/style/index/index.less" scoped lang="less"></style>
<style scoped>
h2 {
  border-bottom: 0px solid #ddd;
  padding-left: 12px;
}



</style>
