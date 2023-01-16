<template>
  <div style="width: 200px; height: 100%; padding-bottom: 48px; overflow: scroll;">
    <a-menu
      :default-selected-keys="[this.$route.path]"
      :default-open-keys="[]"
      @click="handleMenuClick"
      theme="dark"
      mode="inline"
    >
      <template v-for="item in menuData">
        <a-menu-item v-if="!item.children" :key="item.key">
          <a-icon type="appstore" />
          <span>{{ item.title }}</span>
        </a-menu-item>
        <sub-menu v-else :key="item.key" :menu-info="item" />
      </template>
    </a-menu>
  </div>
</template>

<script>

// 参考：https://1x.antdv.com/components/menu-cn/#API

import { Menu } from 'ant-design-vue'
const SubMenu = {
  template: `
      <a-sub-menu :key="menuInfo.key" v-bind="$props" v-on="$listeners">
        <span slot="title">
          <a-icon type="folder" /><span>{{ menuInfo.title }}</span>
        </span>
        <template v-for="item in menuInfo.children">
          <a-menu-item v-if="!item.children" :key="item.key">
            <a-icon type="appstore" />
            <span>{{ item.title }}</span>
          </a-menu-item>
          <sub-menu v-else :key="item.key" :menu-info="item" />
        </template>
      </a-sub-menu>
    `,
  name: 'SubMenu',
  // must add isSubMenu: true
  isSubMenu: true,
  props: {
    ...Menu.SubMenu.props,
    // Cannot overlap with properties within Menu.SubMenu.props
    menuInfo: {
      type: Object,
      default: () => ({})
    }
  }
}
export default {
  name: 'SiderBar',
  components: {
    'sub-menu': SubMenu
  },
  data () {
    return {
      menuData: [
        {
          key: '/admin/overview',
          title: '总览'
        },
        {
          key: '/admin/borrow',
          title: '借阅管理'
        },
        {
          key: '/admin/book',
          title: '图书管理'
        },
        {
          key: '/admin/classification',
          title: '分类管理'
        },
        {
          key: '/admin/tag',
          title: '标签管理'
        },
        {
          key: '/admin/comment',
          title: '评论管理'
        },
        {
          key: '/admin/user',
          title: '系统管理',
          children: [
            {
              key: '/admin/user',
              title: '用户管理'
            },
            {
              key: '/admin/loginLog',
              title: '登录日志'
            },
            {
              key: '/admin/opLog',
              title: '操作日志'
            },
            {
              key: '/admin/borrowLog',
              title: '借阅日志'
            }
          ]
        }
      ]
    }
  },
  methods: {
    handleMenuClick ({ item, key, keyPath }) {
      if (key !== this.$route.path) {
        this.$router.push(key)
      }
    }
  }
}
</script>
