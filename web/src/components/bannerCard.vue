<template>
  <a-carousel autoplay>
    <template v-for="item in bannerData">
      <div class="b-item"><img src="https://pic.arkread.com/banner/campaign/u/13511.1671069236!campaign.png"/></div>
    </template>
  </a-carousel>
</template>
<script>
export default {
  name: 'BannerCard',
  data () {
    return {
      bannerData: ['1', '1', '1', '1', '1']
    }
  }
}
</script>

<style scoped lang="less">

.ant-carousel {
  text-align: center;
  height: 200px;
  background: #364d79;
  overflow: hidden;
}

.b-item{
  height: 200px;
  z-index: -99;
}
img {
  width: 100%;
  height: 100%;
  background-size: 100% 100%;
  background-repeat: no-repeat;
}
.ant-carousel .slick-dots-bottom {
  bottom: 30px;
}

</style>
