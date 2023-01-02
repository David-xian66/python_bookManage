<template>
  <div>
    <h1>图书标签: 小说</h1>
    <div class="article">
      <div id="subject_list">
        <div class="clearfix">
        <span class="rr greyinput">综合排序 &nbsp;/&nbsp;
          <a href="#">按出版日期排序</a>&nbsp;/&nbsp;
          <a href="#">按评价排序</a>
        </span>
        </div>
        <ul class="subject-list">
          <template v-for="item in data">
            <li class="subject-item">
              <div class="pic">
                <a class="nbg" href="#">
                  <img class="" src="https://pic.arkread.com/cover/ebook/f/400668268.1657173376.jpg!cover_default.jpg" width="90">
                </a>
              </div>
              <div class="info">
                <h2 class="">
                  <a href="#" title="长安的荔枝">长安的荔枝</a>
                </h2>
                <div class="pub">马伯庸 / 湖南文艺出版社 / 2022-10 / 45.00元</div>
                <div class="star clearfix">
              <span class="allstar45">
              </span>
                  <span class="rating_nums">8.5</span>
                  <span class="pl">(31451人评价)</span>
                </div>
                <p>大唐天宝十四年，长安城的小吏李善德突然接到一个任务：要在贵妃诞日之前，从岭南运来新鲜荔枝。荔枝“一日色变，两日香变，三日味变”，而岭南距长安五千余里，山水迢...</p>
                <div class="ft">
                  <div class="collect-info">
                  </div>
                  <div class="cart-actions">
                <span class="buy-info">
                  <a href="">纸质版 26.80元</a>
                </span>
                    <span class="cart-info">
                  <span class="add2cartWidget ">
                    <a href="javascript:;" class="j  a_add2cart add2cart" name="36104107">
                      <span>加入购书单</span>
                    </a>
                  </span>
                </span>
                  </div>
                </div>
              </div>
            </li>
          </template>
        </ul>
        <div class="paginator">
          <a-pagination size="small" :default-current="6" :total="100" />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'BookListCard',
  data () {
    return {
      data: ['1', '1', '1', '1', '1', '1']
    }
  }
}
</script>
<style src="@/style/index/index.less" scoped lang="less"></style>
<style scoped>
h2 {
  border-bottom: 0px solid #ddd;
}
h1 {
  word-wrap: break-word;
  display: block;
  font-size: 25px;
  font-weight: bold;
  color: #494949;
  margin: 0;
  padding: 0 0 15px 0;
  line-height: 1.1;
}

</style>
