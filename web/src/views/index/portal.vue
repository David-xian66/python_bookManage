<template>

  <div id="portal">
    <a-layout>
      <a-layout>
        <NavCard />
      </a-layout>
      <a-layout-content>
        <div class="content">
          <div class="left">
            <BannerCard />
            <HotCard />
            <LastCard />
            <HotReviewCard />
          </div>
          <div class="right">
            <TagCard />
            <HotBorrowCard />
          </div>
        </div>
      </a-layout-content>
      <a-layout-footer>
        <FooterCard />
      </a-layout-footer>
    </a-layout>
  </div>
</template>

<script>
import HotCard from '@/components/hotCard'
import TagCard from '@/components/tagCard'
import HotReviewCard from '@/components/hotReviewCard'
import BannerCard from '@/components/bannerCard'
import LastCard from '@/components/lastCard'
import HotBorrowCard from '@/components/hotBorrowCard'
import FooterCard from '@/components/footerCard'
import NavCard from "@/components/navCard";

export default {
  name: 'Portal',
  components: {
    NavCard,
    FooterCard,
    HotBorrowCard,
    LastCard,
    BannerCard,
    HotReviewCard,
    HotCard,
    TagCard
  }
}
</script>

<style scoped>
.content {
  margin: 0 auto;
  width: 1010px;
  display: flex;
  flex-direction: row;
  gap: 25px;
}
.left {
  position: relative;
  width: 675px;
  display: flex;
  flex-direction: column;
  gap: 30px;
}
.right {
  width: 300px;
  display: flex;
  flex-direction: column;
  flex:1;
  gap: 30px;
}

#portal {}
#portal .ant-layout{
  background: #fff;
}
#portal .ant-layout-footer {
  background: #fff;
}
#portal .ant-layout-footer {
  line-height: 1.5;
}
#portal .ant-layout-content {
  background: #fff;
}
#portal > .ant-layout {
  margin-bottom: 48px;
}
</style>
