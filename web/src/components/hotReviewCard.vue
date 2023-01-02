<template>
  <div id="reviews" class="section"><div class="reviews-hd">
    <h2 class="fw">
      热门书评
      <span><a href="/review/best/">更多热门书评»</a></span>
    </h2>
  </div>
    <div class="reviews-bd">

      <template v-for="item in hotReviewData">

        <div class="review ">
          <div class="review-hd">
            <a href="https://book.douban.com/review/13955731/">
              <img src="https://pic.arkread.com/cover/ebook/f/399488285.1656307735.jpg!cover_default.jpg" alt="100%受欢迎的说话技巧，高效沟通者的必读书">
            </a>
          </div>
          <div class="review-bd">
            <h3><a href="https://book.douban.com/review/13955731/">100%受欢迎的说话技巧，高效沟通者的必读书</a></h3>
            <div class="review-meta">
              <a href="https://www.douban.com/people/103126511/">且听风吟xl</a> 评论
              <a href="https://book.douban.com/review/13955731/">《高效沟通》</a>

              <span class="allstar40"></span>
            </div>
            <div class="review-content">
              记得听过这样一个笑话： 古时候，英雄救了美女。 如果英雄帅，美女就说英雄救命之恩，小女子无以为报，唯有以身相许； 如果英雄不帅，姑娘就会说，英雄救命之恩，小女子无以为报，唯有来生做牛做马来报答。 这个...
              <a href="https://book.douban.com/review/13955731/">(全文)</a>
            </div>
          </div>
        </div>

      </template>
    </div></div>
</template>
<script>
export default {
  name: 'HotReviewCard',
  data () {
    return {
      hotReviewData: ['1', '1', '1', '1', '1']
    }
  }
}
</script>
<style src="@/style/index/index.less" scoped lang="less"></style>
