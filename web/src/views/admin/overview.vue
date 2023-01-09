<template>

  <div class="main">
<!--        <div>-->
<!--          业务1..{{ $store.state.user.name }}..{{ $store.getters.name }}-->
<!--          <a-button type="primary" @click="handleLogout">退出登录</a-button>-->
<!--        </div>-->

    <a-row :gutter="24">
      <a-col :span="6">
        <div class="box" style="background-color: #77c5ee;">
          <div>图书总数</div>
          <div><span class="box-value">{{ data.book_count }}</span>本</div>
        </div>
      </a-col>
      <a-col :span="6">
        <div class="box" style="background-color: #1890ff;">
          <div>在借书籍</div>
          <div><span class="box-value">{{ data.borrow_count }}</span>本</div>
        </div>
      </a-col>
      <a-col :span="6">
        <div class="box" style="background-color: #2a9a44;">
          <div>已还书籍</div>
          <div><span class="box-value">{{ data.return_count }}</span>本</div>
        </div>
      </a-col>
      <a-col :span="6">
        <div class="box" style="background-color: #0EC885;">
          <div>逾期未还</div>
          <div><span class="box-value">{{ data.overdue_count }}</span>本</div>
        </div>
      </a-col>
    </a-row>

    <div class="main-b" style="padding-top: 50px;" ref="chartWrap">
      <div style="flex:1;height: 100%;padding: 30px 30px;" ref="barChart"></div>
      <div style="flex:1;;height: 100%; padding: 30px 30px;" ref="pieChart"></div>
    </div>

  </div>

</template>

<script>
import * as echarts from 'echarts'
import {listApi} from '@/api/overview'
import storage from 'store'
import {USER_NAME, ACCESS_TOKEN} from '@/store/constants'

export default {
  name: 'One',
  data () {
    return {
      barChart: undefined,
      pieChart: undefined,
      data: {}
    }
  },
  mounted () {
    // this.$store.commit('SET_NAME', 'zhangsan')
    // this.$store.dispatch('Login', 'linxiaomei')

    console.log(this.$store.state.user.name)
    console.log(this.$store.getters.name)

    console.log(storage.get(USER_NAME))
    console.log(storage.get(ACCESS_TOKEN))
    this.list()
    const that = this
    setTimeout(function () {
      that.$refs.chartWrap.style.height = '70%'
      that.initBarChart()
      that.initPieChart()
    }, 100)

    window.onresize = function () { // resize
      that.barChart.resize()
      that.pieChart.resize()
    }
  },
  methods: {
    handleLogout () {
      this.$store.dispatch('Logout').then(res => {
        this.$router.push({name: 'login'})
      })
    },
    list () {
      listApi({}).then(res => {
        console.log(res.data)
        this.data = res.data
      }).catch(err => {
        this.$message.error(err.data || '获取失败！')
      })
    },
    initBarChart () {
      let xData = []
      let yData = []
      this.data.borrow_rank_data.forEach((item, index) => {
        xData.push(item.title)
        yData.push(item.count)
      })
      // const xData = ['遥远的救世主', '平凡的世界', '测试书籍12', '测试书籍13', '测试书籍14', '测试书籍15', '测试书籍16', '测试书籍17']
      // const yData = [220, 200, 180, 150, 130, 110, 100, 80]
      this.barChart = echarts.init(this.$refs.barChart)
      let option = {
        title: {
          text: '热门借阅排名',
          x: 'center',
          y: 'top'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        xAxis: {
          data: xData,
          type: 'category',
          axisLabel: {
            rotate: 30, // 倾斜30度,
            textStyle: {
              color: '#2F4F4F'
            }
          },
          axisLine: {
            lineStyle: {
              color: '#2F4F4F'
            }
          }
        },
        yAxis: {
          type: 'value',
          axisLine: {
            lineStyle: {
              color: '#2F4F4F'
            }
          }
        },
        series: [
          {
            data: yData,
            type: 'bar',
            itemStyle: {
              normal: {
                color: function (params) {
                  // 柱图颜色
                  const colorList = ['#c23531', '#61a0a8', '#d48265', '#91c7ae', '#749f83', '#ca8622']
                  let index = params.dataIndex
                  if (params.dataIndex >= colorList.length) {
                    index = params.dataIndex - colorList.length
                  }
                  return colorList[index]
                }
              }
            }
          }
        ]
      }
      this.barChart.setOption(option)
    },
    initPieChart () {
      let pieData = []
      this.data.classification_rank_data.forEach((item, index) => {
        pieData.push({name:item.title, value:item.count})
      })
      this.pieChart = echarts.init(this.$refs.pieChart)
      const option = {
        title: {
          text: '热门分类比例',
          x: 'center',
          y: 'top'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          top: '90%',
          left: 'center'
        },
        series: [
          {
            name: '分类',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 20,
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: pieData
          }
        ]
      }
      this.pieChart.setOption(option)
    }
  }
}
</script>

<style lang="less" scoped>

.main {
  //background-color: #1890ff;
  height: 100%;
  display: flex;
  flex-direction: column;

  .box {
    display: flex;
    flex-direction: column;
    gap: 12px;
    padding: 20px;
    border-radius: 8px;
    color: #FFFFFF;
    font-size: 14px;
    //background-color: #00aaeb;

    .box-value {
      font-size: 32px;
    }
  }

  .main-b {
    position: relative;
    display: flex;
    flex-direction: row;
    flex-shrink: 0;
  }
}

</style>
