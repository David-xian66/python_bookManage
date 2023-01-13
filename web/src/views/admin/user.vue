<template>
  <div class="page-view">
    <div class="table-operation">
      <a-space>
        <a-button type="primary" @click="handleAdd">新增</a-button>
        <a-button @click="handleBatchDelete">批量删除</a-button>
        <a-input-search addon-before="用户名" enter-button @search="onSearch" @change="onSearchChange" />
      </a-space>
    </div>
    <div class="table-wrap" ref="tableWrap">
      <a-table
        size="middle"
        rowKey="id"
        :loading="loading"
        :columns="columns"
        :data-source="data"
        :scroll="{ x: 'max-content' }"
        :row-selection="rowSelection()"
        :pagination="{
          size: 'default',
          current: page,
          pageSize: pageSize,
          onChange: (current) => page = current,
          pageSizeOptions: ['10', '20', '30', '40'],
          showSizeChanger: true,
          showTotal: (total) => `共${total}条数据`
        }"
      >
        <span slot="operation" class="operation" slot-scope="text, record">
          <a-space :size="16">
            <a @click="handleEdit(record)">编辑</a>
            <a @click="handleDelete(record)">删除</a>
          </a-space>
        </span>
      </a-table>
    </div>
  </div>
</template>

<script>
import {listApi, deleteApi} from '@/api/admin/user'
import EditUser from '@/views/admin/model/edit-user'

const columns = [
  {
    title: '序号',
    dataIndex: 'index',
    key: 'index',
    width: 60
  },
  {
    title: '用户名',
    dataIndex: 'username',
    key: 'username'
  },
  {
    title: '昵称',
    dataIndex: 'nickname',
    key: 'nickname'
  },
  {
    title: '角色',
    dataIndex: 'role',
    key: 'role',
    customRender: (text) => text === '0' ? '管理员' : '普通用户'
  },
  {
    title: '状态',
    dataIndex: 'status',
    key: 'status',
    customRender: (text) => text === '0' ? '正常' : '封号'
  },
  {
    title: '邮箱',
    dataIndex: 'email',
    key: 'email'
  },
  {
    title: '手机号',
    dataIndex: 'mobile',
    key: 'mobile'
  },
  {
    title: '创建时间',
    dataIndex: 'create_time',
    key: 'create_time'
  },
  {
    title: '操作',
    dataIndex: 'action',
    align: 'right',
    fixed: 'right',
    width: 140,
    scopedSlots: { customRender: 'operation' }
  }
]

export default {
  name: 'User',
  data () {
    return {
      loading: false,
      keyword: '',
      selectedRowKeys: [],
      columns,
      data: [],
      pageSize: 10,
      page: 1
    }
  },
  methods: {
    getList () {
      this.loading = true
      listApi({
        keyword: this.keyword
      }).then(res => {
        this.loading = false
        res.data.forEach((item, index) => {
          item.index = index + 1
        })
        this.data = res.data
        console.log(res)
      })
    },
    onSearchChange (e) {
      this.keyword = e.target.value
    },
    onSearch (value) {
      this.getList()
    },
    rowSelection () {
      return {
        onChange: (selectedRowKeys, selectedRows) => {
          this.selectedRowKeys = selectedRowKeys
        }
      }
    },
    handleAdd () {
      this.$dialog(
        EditUser,
        {
          on: {
            ok: () => {
              this.page = 1
              this.getList()
            }
          }
        },
        {
          title: '新增用户',
          width: '480px',
          centered: true,
          bodyStyle: {
            maxHeight: 'calc(100vh - 200px)',
            overflowY: 'auto'
          }
        }
      )
    },
    handleEdit (record) {
      this.$dialog(
        EditUser,
        {
          user: Object.assign({}, record),
          modifyFlag: true,
          on: {
            ok: () => {
              this.getList()
            }
          }
        },
        {
          title: '编辑用户',
          width: '480px',
          centered: true,
          bodyStyle: {
            maxHeight: 'calc(100vh - 200px)',
            overflowY: 'auto'
          }
        }
      )
    },
    // 删除
    handleDelete (record) {
      const that = this
      this.$confirm({
        title: '确定删除?',
        onOk () {
          deleteApi({
            ids: record.id
          }).then(res => {
            that.$message.success('删除成功')
            that.getList()
          }).catch(err => {
            that.$message.error(err.msg || '删除失败')
          })
        }
      })
    },
    // 批量删除
    handleBatchDelete () {
      console.log(this.selectedRowKeys)
      if (this.selectedRowKeys.length <= 0) {
        this.$message.warn('请勾选删除项')
        return
      }
      const that = this
      this.$confirm({
        title: '确定删除?',
        onOk () {
          deleteApi({
            ids: that.selectedRowKeys.join(',')
          }).then(res => {
            that.$message.success('删除成功')
            that.selectedRowKeys = []
            that.getList()
          }).catch(err => {
            that.$message.error(err.msg || '删除失败')
          })
        }
      })
    }
  },
  mounted () {
    this.getList()
  }
}
</script>

<style lang="less" scoped>
.table-wrap {
  flex: 1;
}
.page-view {
  min-height: 100%;
  background: #FFF;
  padding: 8px;
  display: flex;
  flex-direction: column;
}
.table-operation {
  height: 50px;
  text-align: right;
}
</style>
