<template>
  <div class="block5">

    <h2 class="">
      <span class="">你可能感兴趣的图书</span>
      <span class="link-more">
        <a class="" href="/recommended?icn=index-book250-all">更多»</a>
      </span>
    </h2>


    <div class="content clearfix s" id="book_rec" data-dstat-areaid="59" data-dstat-mode="click,expose">

    <template v-for="item in recommendData">
      <dl>
        <dt>
          <a>
            <img src="https://pic.arkread.com/cover/ebook/f/400668268.1657173376.jpg!cover_default.jpg" class="m_sub_img">
          </a>
        </dt>
        <dd>
          <a>
            我存在
          </a>
        </dd>
      </dl>
    </template>


    </div>
  </div>
</template>
<script>
export default {
  name: 'RecommendCard',
  data() {
    return {
      recommendData: ['1', '1', '1', '1', '1', '1', '1', '1', '1']
    }
  }
}
</script>

<style src="@/style/index/index.less" scoped lang="less"></style>
