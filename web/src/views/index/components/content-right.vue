<template>
  <div class="content-right">
    <div class="pc-search-view flex-view">
      <img src="@/assets/searchIcon.svg"
           alt="搜索" class="search-icon">
      <input placeholder="搜索书名、ISBN" ref="keyword">
      <img src="@/assets/clear-search.svg" alt="清空" @click="clearSearch" class="clear-search-icon">
      <button @click="search">搜索</button>
      <span class="float-count" style="">共有2005本图书</span>
    </div>
    <div class="top-select-view flex-view">
      <div class="type-view">
        <span class="type-tab"
              :class="selectTypeIndex===index? 'type-tab-select':''"
              v-for="(item,index) in typeData"
              :key="index"
              @click="selectType(index)">
          {{item}}
        </span>
        <span :style="{left: typeUnderLeft + 'px'}" class="tab-underline"></span>
      </div>
      <div class="order-view">
        <span class="title">排序方式：</span>
        <span class="tab"
              :class="selectTabIndex===index? 'tab-select':''"
              v-for="(item,index) in tabData"
              :key="index"
              @click="selectTab(index)">
          {{item}}
        </span>
        <span :style="{left: tabUnderLeft + 'px'}" class="tab-underline"></span>
      </div>
    </div>
    <div class="pc-book-list flex-view">
      <div v-for="item in bookData" class="book-item item-column-3"><!---->
        <div class="img-view"><img class=""
                                   data-src="https://file.ituring.com.cn/LargeCover/2212c21242c05ebc49f3"
                                   src="https://file.ituring.com.cn/LargeCover/2212c21242c05ebc49f3"
                                   lazy="loaded"></div>
        <div class="info-view"><h3 class="book-name">可编程网络自动化</h3>
          <p class="authors">menjiaLi qiao jun</p>
          <p class="translators">门佳，李巧君（译者）</p></div>
      </div>
      <div class="no-data" style="display: none;">没有搜索到结果</div>
    </div>
    <div class="page-view" style="">
      <a-pagination v-model="page" size="small" :total="50"/>
    </div>

  </div>
</template>

<script>
export default {
  name: 'ContentRight',
  data () {
    return {
      page: 1,
      typeData: ['纸质书', '电子书', '预售书'],
      selectTypeIndex: 0,
      typeUnderLeft: 22,
      tabData: ['最新', '最热', '推荐'],
      selectTabIndex: 0,
      tabUnderLeft: 86,
      bookData: [
        '1',
        '1',
        '1',
        '1',
        '1',
        '1',
        '1',
        '1',
        '1',
        '1',
        '1',
        '1',
        '1',
        '1'
      ]
    }
  },
  methods: {
    search () {
      const keyword = this.$refs.keyword.value
      console.log(keyword)
    },
    clearSearch () {
      this.$refs.keyword.value = ''
      this.search()
    },
    selectType (index) {
      this.selectTypeIndex = index
      this.typeUnderLeft = 22 + 90 * index
    },
    selectTab (index) {
      this.selectTabIndex = index
      this.tabUnderLeft = 86 + 53 * index
    }
  }
}
</script>
<style scoped lang="less">
.content-right {
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;
  padding-top: 24px;

  .pc-search-view {
    margin: 0 0 24px;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;

    .search-icon {
      width: 20px;
      height: 20px;
      -webkit-box-flex: 0;
      -ms-flex: 0 0 20px;
      flex: 0 0 20px;
      margin-right: 16px;
    }

    input {
      outline: none;
      border: 0px;
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      border-bottom: 1px solid #cedce4;
      color: #152844;
      font-size: 14px;
      height: 22px;
      line-height: 22px;
      -ms-flex-item-align: end;
      align-self: flex-end;
      padding-bottom: 8px;
    }

    .clear-search-icon {
      position: relative;
      left: -20px;
      cursor: pointer;
    }

    button {
      outline: none;
      border: none;
      font-size: 14px;
      color: #fff;
      background: #288dda;
      border-radius: 32px;
      width: 88px;
      height: 32px;
      line-height: 32px;
      margin-left: 2px;
    }

    .float-count {
      color: #999;
      margin-left: 24px;
    }
  }

  .flex-view {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
  }

  .top-select-view {
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    height: 40px;
    line-height: 40px;

    .type-view {
      position: relative;
      font-weight: 400;
      font-size: 18px;
      color: #5f77a6;

      .type-tab {
        margin-right: 32px;
        cursor: pointer;
      }

      .type-tab-select {
        color: #152844;
        font-weight: 600;
        font-size: 20px;
      }

      .tab-underline {
        position: absolute;
        bottom: 0;
        //left: 22px;
        width: 16px;
        height: 4px;
        background: #4684e2;
        -webkit-transition: left .3s;
        transition: left .3s;
      }
    }

    .order-view {
      position: relative;
      color: #6c6c6c;
      font-size: 14px;

      .title {
        margin-right: 8px;
      }

      .tab {
        color: #999;
        margin-right: 20px;
        cursor: pointer;
      }

      .tab-select {
        color: #152844;
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

  }

  .pc-book-list {
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;

    .book-item {
      min-width: 255px;
      max-width: 255px;
      position: relative;
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      margin-right: 20px;
      height: fit-content;
      border-radius: 4px;
      overflow: hidden;
      margin-top: 16px;
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

    .no-data {
      height: 200px;
      line-height: 200px;
      text-align: center;
      width: 100%;
      font-size: 16px;
      color: #152844;
    }
  }

  .page-view {
    width: 100%;
    text-align: center;
    margin-top: 48px;
  }
}
</style>
