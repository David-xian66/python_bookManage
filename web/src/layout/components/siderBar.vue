<template>
  <div style="width: 200px; height: 100%;">
    <a-menu
      :default-selected-keys="[this.$route.path]"
      :default-open-keys="[]"
      @click="handleMenuClick"
      theme="dark"
      mode="inline"
    >
      <template v-for="item in menuData">
        <a-menu-item v-if="!item.children" :key="item.key">
          <a-icon type="pie-chart" />
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
          <a-icon type="mail" /><span>{{ menuInfo.title }}</span>
        </span>
        <template v-for="item in menuInfo.children">
          <a-menu-item v-if="!item.children" :key="item.key">
            <a-icon type="pie-chart" />
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
          title: '用户管理'
        },
        {
          key: '3',
          title: 'Navigation 3',
          children: [
            {
              key: '3.1',
              title: 'Navigation 3.1'
            },
            {
              key: '3.2',
              title: 'Navigation 3.2'
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
