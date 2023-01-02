<template>
  <div class="section ebook-area">
    <div class="hd">

      <h2 class="">
        <span class="fw">热门图书</span>
        <span class="link-more">
        <a class="" href="https://read.douban.com/ebooks?dcs=book-intro&amp;dcm=douban" target="_blank">查看全部»</a>
      </span>
      </h2>

    </div>
    <div class="bd">

      <div class="">

        <div class="sub-section ">
          <div class="sub-bd">
            <ul class="list-col list-col5">

              <template v-for="item in cardData">

                <li class="">
                  <div class="cover">
                    <a target="_blank" title="营销管理（第16版）">
                      <img src="https://pic.arkread.com/cover/ebook/f/400668268.1657173376.jpg!cover_default.jpg"
                           alt="营销管理（第16版）" width="106px" height="158px">
                    </a>
                  </div>
                  <div class="info">
                    <div class="title">
                      <a>
                        营销管理（第16版）
                      </a>
                    </div>
                    <div class="price">
                      109.00元
                    </div>
                    <div class="more-meta">
                      <h4 class="title">
                        营销管理（第16版）
                      </h4>
                    </div>
                  </div>
                </li>

              </template>
            </ul>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'HotCard',
  data() {
    return {
      cardData: ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    }
  }
}
</script>
<style src="@/style/index/index.less" scoped lang="less"></style>
