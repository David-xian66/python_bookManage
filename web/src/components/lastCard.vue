<template>
  <div>
    <div class="section popular-books">
      <div class="hd">
        <h2>
          <span class="fw">最新图书</span>
          <span class="tags">
          <span class="link-more">
            <a href="">查看全部»</a>
          </span>
        </span>
        </h2>
      </div>
      <div class="bd">
        <ul class="list-col list-col2 list-summary s" data-dstat-areaid="61" data-dstat-mode="click,expose">

          <template v-for="item in lastData">
            <li class="">
              <div class="cover">
                <a>
                  <img src="https://pic.arkread.com/cover/ebook/f/399488285.1656307735.jpg!cover_default.jpg"
                       alt="长安的荔枝" class="">
                </a>
              </div>
              <div class="info">
                <h4 class="title">
                  <a class="">长安的荔枝</a>
                </h4>
                <p class="entry-star-small">
                  <span class="allstar45 star-img"></span>
                  <span class="average-rating"> 8.5 </span>
                </p>
                <p class="author">
                  作者：马伯庸
                </p>
              </div>
            </li>

          </template>

        </ul>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'LastCard',
  data() {
    return {
      lastData: ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    }
  }
}

</script>
<style src="@/style/index/index.less" scoped lang="less"></style>
<style scoped lang="less">
.info {
  text-align: left;
}
</style>
