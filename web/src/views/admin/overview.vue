<template>

  <div class="main">

    <a-row :gutter="[20,20]">
      <a-col :sm="24" :md="12" :lg="6">
        <a-card size="small" title="图书总数">
          <a-tag color="blue" slot="extra">月</a-tag>
          <div class="box">
            <div class="box-top">
              <span class="box-value">{{ data.book_count }}<span class="v-e">本</span></span>
              <a-icon type="book" theme="twoTone" style="font-size: 24px;"/>
            </div>
            <div class="box-bottom">
              <span>图书总数: 3,000</span>
            </div>
          </div>
        </a-card>
      </a-col>

      <a-col :sm="24" :md="12" :lg="6">
        <a-card size="small" title="在借书籍">
          <a-tag color="green" slot="extra">月</a-tag>
          <div class="box">
            <div class="box-top">
              <span class="box-value">{{ data.borrow_count }}<span class="v-e">本</span></span>
              <a-icon type="book" theme="twoTone" style="font-size: 24px;"/>
            </div>
            <div class="box-bottom">
              <span>在借总数: 3,000</span>
            </div>
          </div>
        </a-card>
      </a-col>

      <a-col :sm="24" :md="12" :lg="6">
        <a-card size="small" title="已还书籍">
          <a-tag color="blue" slot="extra">月</a-tag>
          <div class="box">
            <div class="box-top">
              <span class="box-value">{{ data.return_count }}<span class="v-e">本</span></span>
              <a-icon type="book" theme="twoTone" style="font-size: 24px;"/>
            </div>
            <div class="box-bottom">
              <span>已还总数: 3,000</span>
            </div>
          </div>
        </a-card>
      </a-col>

      <a-col :sm="24" :md="12" :lg="6">
        <a-card size="small" title="逾期未还">
          <a-tag color="green" slot="extra">月</a-tag>
          <div class="box">
            <div class="box-top">
              <span class="box-value">{{ data.overdue_count }}<span class="v-e">本</span></span>
              <a-icon type="book" theme="twoTone" style="font-size: 24px;"/>
            </div>
            <div class="box-bottom">
              <span>逾期总数: 3,000</span>
            </div>
          </div>
        </a-card>
      </a-col>
    </a-row>

    <a-card title="访问量">
      <div style="height: 300px;" ref="visitChart"></div>
    </a-card>

    <a-row :gutter="[20,20]">
      <a-col :sm="24" :md="24" :lg="12">
        <a-card title="热门借阅排名" style="flex:1;">
          <div style="height: 300px;" ref="barChart"></div>
        </a-card>
      </a-col>
      <a-col :sm="24" :md="24" :lg="12">
        <a-card title="热门分类比例" style="flex:1;">
          <div style="height: 300px;" ref="pieChart"></div>
        </a-card>
      </a-col>
    </a-row>

  </div>

</template>

<script>
import * as echarts from 'echarts'
import {listApi} from '@/api/admin/overview'
import storage from 'store'
import {ADMIN_TOKEN} from '@/store/constants'

export default {
  name: 'One',
  data () {
    return {
      visitChart: undefined,
      barChart: undefined,
      pieChart: undefined,
      data: {
        borrow_rank_data: [],
        classification_rank_data: []
      }
    }
  },
  mounted () {
    // this.$store.commit('SET_NAME', 'zhangsan')
    // this.$store.dispatch('Login', 'linxiaomei')

    // console.log(this.$store.state.user.name)
    // console.log(this.$store.getters.name)

    console.log(storage.get(ADMIN_TOKEN))
    this.list()
    const that = this
    window.onresize = function () { // resize
      that.visitChart.resize()
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
        this.initCharts()
      }).catch(err => {
        this.$message.error(err.msg || '获取失败！')
      })
    },
    initCharts () {
      const that = this
      setTimeout(function () {
        that.initVisitChart()
        that.initBarChart()
        that.initPieChart()
      }, 100)
    },
    initVisitChart () {
      const xData = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月','9月', '10月', '11月', '12月']
      const yData = [220, 200, 180, 150, 130, 110, 100, 80,130, 110, 100, 80]
      this.visitChart = echarts.init(this.$refs.visitChart)
      let option = {
        grid: {
          // 让图表占满容器
          top: '40px',
          left: '40px',
          right: '40px',
          bottom: '40px'
        },
        title: {
          text: '',
          textStyle: {
            color: '#AAAAAA',
            fontStyle: 'normal',
            fontWeight: 'normal',
            fontSize: 18
          },
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
          axisLine: {show: false},
          axisTick: {show: false},
          splitLine: {
            show: true, // 网格线
            lineStyle: {
              color: 'rgba(10, 10, 10, 0.1)',
              width: 1,
              type: 'solid'
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
                  return '#58A0D5'
                }
              }
            }
          }
        ]
      }
      this.visitChart.setOption(option)
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
        grid: {
          // 让图表占满容器
          top: '40px',
          left: '40px',
          right: '40px',
          bottom: '40px'
        },
        title: {
          text: '近30天借阅排名',
          textStyle: {
            color: '#aaa',
            fontStyle: 'normal',
            fontWeight: 'normal',
            fontSize: 18
          },
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
          axisLine: {show: false},
          axisTick: {show: false},
          splitLine: {
            show: true, // 网格线
            lineStyle: {
              color: 'rgba(10, 10, 10, 0.1)',
              width: 1,
              type: 'solid'
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
                  return '#70B0EA'
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
        pieData.push({name: item.title, value: item.count})
      })
      this.pieChart = echarts.init(this.$refs.pieChart)
      const option = {
        grid: {
          // 让图表占满容器
          top: '40px',
          left: '40px',
          right: '40px',
          bottom: '40px'
        },
        title: {
          text: '近30天热门借阅分类',
          textStyle: {
            color: '#aaa',
            fontStyle: 'normal',
            fontWeight: 'normal',
            fontSize: 18
          },
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
            itemStyle: {
              normal: {
                color: function (params) {
                  const colorList = ['#70B0EA', '#B3A3DA', '#88DEE2', '#62C4C8', '#58A3A1']
                  let index = params.dataIndex
                  if (params.dataIndex >= colorList.length) {
                    index = params.dataIndex - colorList.length
                  }
                  return colorList[index]
                }
              }
            },
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
  height: 100%;
  display: flex;
  gap:20px;
  flex-direction: column;

  .box {
    padding: 12px;
    display: flex;
    flex-direction: column;

    .box-top {
      display: flex;
      flex-direction: row;
      align-items: center;
    }
    .box-value {
      color: #000000;
      font-size: 28px;
      margin-right: 12px;
      .v-e {
        font-size: 14px;
      }
    }

    .box-bottom {
      margin-top: 24px;
      color: #000000d9;
    }
  }
}

</style>
