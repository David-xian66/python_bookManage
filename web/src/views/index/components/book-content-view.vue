<template>
  <div class="book-content-view flex-view">
    <div class="main-content">
      <div class="order-view main-tab">
          <span class="tab"
                :class="selectTabIndex===index? 'tab-select':''"
                v-for="(item,index) in tabData"
                :key="index"
                @click="selectTab(index)">
            {{ item }}
          </span>
        <span :style="{left: tabUnderLeft + 'px'}" class="tab-underline"></span>
      </div>

      <div class="book-intro">
        <p class="text" style="">
          不管是个人，还是企业，要实现目标、获得成功，往往都要先构建自己的竞争优势。有些优势是我们未曾意识到自己本就拥有的，有些优势是我们明确知道自己尚未具备的，但是怎样的优势组合才是真正有效的？本书提出了不公平优势的概念与由5种不公平优势构成的MILES框架，并结合大量案例，介绍了如何利用自己的不公平优势获得商业上的成功，同时，作为成功的创业者，两位作者还非常贴心地提供了快速创业入门指南。
          本书适合个人贡献者和创业者阅读。</p>
      </div>
    </div>
    <div class="recommend" style="">
      <div class="title">大家都在读</div>
      <div class="books">
        <div class="book-item book-item" v-for="item in recommendData">
          <div class="img-view">
            <img src="https://file.ituring.com.cn/LargeCover/22126309ebb8938b0f9e">
          </div>
          <div class="info-view">
            <h3 class="book-name">游戏化思维：从激励到沉浸</h3>
            <p class="authors">王亚晖（作者）</p>
            <p class="translators">刘娜娜（译者）</p>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>
<script>
export default {
  name: 'BookContentView',
  data () {
    return {
      tabUnderLeft: 6,
      tabData: ['简介', '评论'],
      selectTabIndex: 0,
      recommendData: ['', '', '', '', '']
    }
  },
  methods: {
    selectTab (index) {
      this.selectTabIndex = index
      this.tabUnderLeft = 6 + 58 * index
    }
  }
}
</script>
<style scoped lang="less">
.flex-view {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.book-content-view {
  margin-top: 40px;
  padding-bottom: 50px;
}

.main-content {
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;

  .text {
    color: #484848;
    font-size: 16px;
    line-height: 26px;
    padding-left: 12px;
    margin: 11px 0;
    white-space: pre-wrap;
  }
}

.main-tab {
  border-bottom: 1px solid #cedce4;
}

.order-view {
  position: relative;
  color: #6c6c6c;
  font-size: 14px;
  line-height: 40px;

  .title {
    margin-right: 8px;
  }

  .tab {
    margin-right: 20px;
    cursor: pointer;
    color: #5f77a6;
    font-size: 16px;
    cursor: pointer;
  }

  .tab-select {
    color: #152844;
    font-weight: 600;
  }

  .tab-underline {
    position: absolute;
    bottom: 0;
    left: 84px;
    width: 16px;
    height: 4px;
    background: #4684e2;
    -webkit-transition: left .3s;
    transition: left .3s;
  }
}

.recommend {
  -webkit-box-flex: 0;
  -ms-flex: 0 0 235px;
  flex: 0 0 235px;
  margin-left: 20px;

  .title {
    font-weight: 600;
    font-size: 18px;
    line-height: 26px;
    color: #152844;
    margin-bottom: 12px;
  }

  .books {
    border-top: 1px solid #cedce4;

    .book-item {
      position: relative;
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      min-width: 255px;
      max-width: 255px;
      margin: 16px 0;
      height: fit-content;
      border-radius: 4px;
      overflow: hidden;
      cursor: pointer;

      .img-view {
        background: #eaf1f5;
        font-size: 0;
        text-align: center;
        height: 156px;
        padding: 8px 0;

        img {
          height: 100%;
          display: block;
          margin: 0 auto;
          border-radius: 4px;
          -webkit-box-sizing: border-box;
          box-sizing: border-box;
        }
      }

      .info-view {
        background: #f6f9fb;
        text-align: center;
        height: 108px;
        overflow: hidden;
        padding: 0 16px;

        h3 {
          color: #1c355a;
          font-weight: 500;
          font-size: 16px;
          line-height: 20px;
          overflow: hidden;
          text-overflow: ellipsis;
          display: -webkit-box;
          -webkit-line-clamp: 2;
          -webkit-box-orient: vertical;
          margin: 12px 0 8px;
        }

        .authors {
          color: #6f6f6f;
          font-size: 12px;
          line-height: 14px;
          margin-top: 4px;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
        }

        .translators {
          color: #6f6f6f;
          font-size: 12px;
          line-height: 14px;
          margin-top: 4px;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
        }
      }
    }
  }
}
</style>
