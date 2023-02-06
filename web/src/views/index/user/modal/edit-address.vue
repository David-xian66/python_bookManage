<template>
  <a-form-model
    ref="myform"
    :model="form"
    :rules="rules">
    <a-row :gutter="24">
      <a-col span="24">
        <a-form-model-item label="姓名" prop="title">
          <a-input placeholder="请输入" v-model="form.name"></a-input>
        </a-form-model-item>
      </a-col>
    </a-row>
    <a-row :gutter="24">
      <a-col span="24">
        <a-form-model-item label="电话号码" prop="title">
          <a-input placeholder="请输入" v-model="form.mobile"></a-input>
        </a-form-model-item>
      </a-col>
    </a-row>
    <a-row :gutter="24">
      <a-col span="24">
        <a-form-model-item label="送货地址" prop="title">
          <a-input placeholder="请输入" v-model="form.addressDesc"></a-input>
        </a-form-model-item>
      </a-col>
    </a-row>
    <a-row :gutter="24">
      <a-col span="24">
        <a-form-model-item label="默认地址" prop="title">
          <a-switch v-model="form.default"></a-switch>
        </a-form-model-item>
      </a-col>
    </a-row>
  </a-form-model>
</template>

<script>
// import {createApi, updateApi} from '@/api/admin/classification'

export default {
  name: 'EditAddress',
  props: {
    modifyFlag: {
      type: Boolean,
      default: () => false
    }
  },
  data () {
    return {
      form: {
        title: undefined
      }
    }
  },
  created () {
  },
  methods: {
    onOk () {
      return new Promise((resolve, reject) => {
        console.log(this.form)
        this.$refs.myform.validate(valid => {
          if (valid) {
          }
        })
      })
    }
  }
}
</script>

<style lang="less" scoped>

</style>
