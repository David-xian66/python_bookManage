<template>
  <div class="container">

    <div  class="tel-regist-page pc-style">
      <div  class="regist-title">
        <span >注册新账号</span>
        <span  role="button" class="toWxLogin">我要登录</span>
      </div>
      <div  class="regist-padding">
        <div   class="common-input">
          <img  src="@/assets/register-name.svg" class="left-icon">
          <div  class="input-view">
            <input  placeholder="请设定昵称，最多12个字符" length="12" type="text" class="input">
            <p  class="err-view">
            </p>
          </div>
          <img  src="" class="right-icon" style="display: none;">
          <!---->
        </div>
      </div>
      <div   class="tel-login">
        <div   class="common-input">
          <img  src="@/assets/tel-icon.svg" class="left-icon">
          <div  class="input-view">
            <input  placeholder="请输入手机号" length="11" type="number" class="input">
            <p  class="err-view">
            </p>
          </div>
          <img  src="" class="right-icon" style="display: none;">
          <!---->
        </div>
        <div  class="next-btn-view">
          <button class="next-btn" style="margin: 16px 0px;">下一步</button>
        </div>
        <div  class="loading" style="display: none;">
          <div class="content tl-detail-loading">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="less">
div {
  display: block;
}
*, :after, :before, img {
  border-style: solid;
}

*, :after, :before {
  border-width: 0;
  border-color: #dae1e7;
}

.container {
  max-width: 100%;
}

.pc-style {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  width: 400px;
  height: 464px;
  background: #fff;
  -webkit-box-shadow: 0 8px 16px rgb(0 0 0 / 8%);
  box-shadow: 0 8px 16px rgb(0 0 0 / 8%);
  border-radius: 4px;
  margin: -232px auto 0;
}

.tel-regist-page {
  overflow: hidden;
  .regist-title {
    font-size: 14px;
    color: #1e1e1e;
    font-weight: 500;
    height: 24px;
    line-height: 24px;
    margin: 40px 0;
    padding: 0 28px;
    .toWxLogin {
      color: #3d5b96;
      float: right;
    }
  }
  .regist-padding {
    padding: 0 28px;
    margin-bottom: 8px;
  }
}

.common-input {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: start;
  -ms-flex-align: start;
  align-items: flex-start;
  .left-icon {
    margin-right: 12px;
    width: 24px;
  }
  .input-view {
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    .input {
      font-weight: 500;
      font-size: 14px;
      color: #1e1e1e;
      height: 26px;
      line-height: 26px;
      border: none;
      padding: 0;
      display: block;
      width: 100%;
      letter-spacing: 1.5px;
    }
    .err-view {
      margin-top: 4px;
      height: 16px;
      line-height: 16px;
      font-size: 12px;
      color: #f62a2a;
    }
  }
}

.tel-login {
  padding: 0 28px;
}
.next-btn {
  background: #c3c9d5;
  border-radius: 4px;
  color: #fff;
  font-size: 14px;
  font-weight: 500;
  height: 40px;
  line-height: 40px;
  text-align: center;
  width: 100%;
  outline: none;
}

</style>
