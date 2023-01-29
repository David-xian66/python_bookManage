<template>
  <div class="content-left">
    <div class="left-search-item"><h4>图书分类</h4>
      <div class="category-item">
        <div class="flex-view">
          <span class="name">全部</span>
          <span class="count"></span>
        </div>
      </div>
      <template v-for="item in data">
        <div class="category-item">
          <div class="flex-view" @click="toggleShow($event)">
            <span class="name">{{ item.name }}</span>
            <span class="count">11</span>
          </div>
          <ul style="display: none;">
            <template v-for="child in item.children">
              <li class="child">{{ child.name }}</li>
            </template>
          </ul>
        </div>
      </template>
    </div>
    <div class="left-search-item"><h4>书籍状态</h4>
      <div class="check-item flex-view"><input type="checkbox" name="state"
                                               id="state0" value="上市销售"><label
        for="state0">上市销售</label>
      </div>
      <div class="check-item flex-view"><input type="checkbox" name="state"
                                               id="state1" value="诚招译者"><label
        for="state1">诚招译者</label>
      </div>
      <div class="check-item flex-view"><input type="checkbox" name="state"
                                               id="state2" value="正在翻译"><label
        for="state2">正在翻译</label>
      </div>
    </div>
    <div class="left-search-item"><h4>热门标签</h4>
      <div class="tag-view tag-flex-view">
        <div v-for="item in tagData" :key="item.id">
          <span class="tag">{{item.title}}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {listApi} from '@/api/index/classification'
import {listApi as listTagList} from '@/api/index/tag'

export default {
  name: 'ContentLeft',
  data () {
    return {
      data: [],
      tagData: [],
      loading: false
    }
  },
  mounted () {
    this.getList()
  },
  methods: {
    getList () {
      listApi().then(res => {
        this.data = res.data
      })
      listTagList().then(res => {
        this.tagData = res.data
      })
    },
    // 显示/隐藏
    toggleShow (e) {
      let next = e.currentTarget.nextElementSibling
      let display = next.style.display
      if (display === 'none') {
        display = 'block'
      } else {
        display = 'none'
      }
      next.style.display = display
    }
  }
}

</script>

<style scoped>

.content-left {
  width: 220px;
  margin-right: 32px;
}

.left-search-item {
  overflow: hidden;
  border-bottom: 1px solid #cedce4;
  margin-top: 24px;
  padding-bottom: 24px;
}

h4 {
  color: #4d4d4d;
  font-weight: 600;
  font-size: 16px;
  line-height: 24px;
  height: 24px;
}

.category-item {
  cursor: pointer;
  color: #333;
  margin: 12px 0 0;
  padding-left: 16px;
}

ul {
  margin: 0;
  padding: 0;
}

ul {
  list-style-type: none;
}

li {
  margin: 4px 0 0;
  display: list-item;
  text-align: -webkit-match-parent;
}

.child {
  color: #333;
  padding-left: 16px;
}
.child:hover {
  color: #4684e2;
}

.select {
  color: #4684e2;
}

.flex-view {
  -webkit-box-pack: justify;
  -ms-flex-pack: justify;
  justify-content: space-between;
  display: flex;
}

.name {
  font-size: 14px;
}
.name:hover {
  color: #4684e2;
}

.count {
  font-size: 14px;
  color: #999;
}

.check-item {
  font-size: 0;
  height: 18px;
  line-height: 12px;
  margin: 12px 0 0;
  color: #333;
  cursor: pointer;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}

.check-item input {
  cursor: pointer;
}

.check-item label {
  font-size: 14px;
  margin-left: 12px;
  cursor: pointer;
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;
}

.tag-view {
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  margin-top: 4px;
}

.tag-flex-view {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.tag {
  background: #fff;
  border: 1px solid #a1adc5;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  border-radius: 16px;
  height: 20px;
  line-height: 18px;
  padding: 0 8px;
  margin: 8px 8px 0 0;
  cursor: pointer;
  font-size: 12px;
  color: #152844;
}
</style>
