<template>
  <div class="main-bar-view">
    <div class="search-entry">
      <img src="@/assets/search-icon.svg" class="search-icon">
      <input placeholder="输入关键词" ref="keyword" @keyup.enter="search" />
    </div>
    <div class="right-view">
      <button class="login btn hidden-sm" @click="goLogin()">登录</button>
      <img src="@/assets/avatar.jpg" class="self-img">
      <div class="right-icon">
        <img src="@/assets/cart-icon.svg">
        <span>3</span>
      </div>
      <div class="right-icon">
        <img src="@/assets/message-icon.svg">
        <span class="msg-point" style=""></span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {}
  },
  methods: {
    search () {
      const keyword = this.$refs.keyword.value
      console.log(keyword)
    },
    goLogin () {
      this.$router.push({name: ''})
    }

  }
}
</script>

<style scoped lang="less">
.main-bar-view {
  position: fixed;
  top: 0;
  left: 0;
  height: 56px;
  width: 100%;
  background: #fff;
  border-bottom: 1px solid #cedce4;
  padding-left: 48px;
  z-index: 16;
  display: flex;
  flex-direction: row;
  //justify-content: center; /*水平居中*/
  align-items: center; /*垂直居中*/
}

.search-entry {
  position: relative;
  width: 400px;
  min-width: 200px;
  height: 32px;
  background: #ecf3fc;
  padding: 0 12px;
  border-radius: 16px;
  font-size: 0;
  cursor: pointer;

  img {
    max-width: 100%;
    height: auto;
  }
  .search-icon {
    width: 18px;
    margin: 7px 8px 0 0;
  }
  input {
    position: absolute;
    top:4px;
    width: 85%;
    height: 24px;
    border: 0px;
    outline:none;
    color: #000;
    background: #ecf3fc;
    font-size: 14px;
  }
}

.right-view {
  padding-right: 36px;
  flex:1;
  display: flex;
  flex-direction: row;
  gap: 20px;
  justify-content: flex-end; /* 内容右对齐 */
  button {
    outline: none;
    border: none;
    cursor: pointer;
  }
  img {
    cursor: pointer;
  }
  .right-icon {
    position: relative;
    width: 24px;
    margin: 4px 0 0 4px;
    cursor: pointer;
    display: inline-block;
    font-size: 0;
    span {
      position: absolute;
      right: -15px;
      top: -3px;
      font-size: 12px;
      color: #fff;
      background: #4684e2;
      border-radius: 8px;
      padding: 0 4px;
      height: 16px;
      line-height: 16px;
      font-weight: 600;
      min-width: 20px;
      text-align: center;
    }
    .msg-point {
      position: absolute;
      right: -4px;
      top: 0;
      min-width: 8px;
      width: 8px;
      height: 8px;
      background: #4684e2;
      border-radius: 50%;
    }
  }

  .self-img {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    vertical-align: middle;
    cursor: pointer;
  }
  .btn {
    background: #4684e2;
    font-size: 14px;
    color: #fff;
    border-radius: 32px;
    text-align: center;
    width: 66px;
    height: 32px;
    line-height: 32px;
    vertical-align: middle;
    margin-left: 32px;
  }
}

</style>
