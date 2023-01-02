<template>

  <div id="list">
    <a-layout>
      <a-layout>
        <NavCard />
      </a-layout>
      <a-layout-content>
        <div class="content">
          <div class="left">
            <InfoCard />
            <CommentCard />
          </div>
          <div class="right">
            <div class="re-card">
              <RecommendCard />
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
import InfoCard from '@/components/infoCard'
import CommentCard from '@/components/commentCard'
import RecommendCard from '@/components/recommendCard'
import FooterCard from '@/components/footerCard'
import NavCard from '@/components/navCard'

export default {
  name: 'Detail',
  components: {
    NavCard,
    FooterCard,
    InfoCard,
    CommentCard,
    RecommendCard
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

.re-card {
  margin-top: 0px;
}
</style>
