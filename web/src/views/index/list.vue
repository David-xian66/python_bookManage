<template>

  <div id="list">
    <a-layout>
      <a-layout>
        <NavCard />
      </a-layout>
      <a-layout-content>
        <div class="content">
          <div class="left">
            <BookListCard />
          </div>
          <div class="right">
            <div class="top-card">
              <TopCard />
            </div>
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
import BookListCard from '@/components/bookListCard'
import TopCard from "@/components/topCard";

export default {
  name: 'List',
  components: {
    TopCard,
    BookListCard,
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
  width: 1070px;
  display: flex;
  flex-direction: row;
  gap: 80px;
}
.left {
  position: relative;
  width: 675px;
  display: flex;
  flex-direction: column;
  gap: 30px;
}
.right {
  width: 320px;
  display: flex;
  flex-direction: column;
  flex:1;
  gap: 30px;
}

#list {}
#list .ant-layout{
  background: #fff;
}
#list .ant-layout-footer {
  background: #fff;
}
#list .ant-layout-footer {
  line-height: 1.5;
}
#list .ant-layout-content {
  background: #fff;
}
#list > .ant-layout {
  margin-bottom: 48px;
}

.top-card {
  margin-top: 40px;
}
</style>
