<template>
  <div class="container">
    <div class="login-page pc-style">
      <img src="@/assets/logo.png" alt="logo" class="logo-icon">
      <div class="login-tab">
        <div role="tab" class="tab-selected">
          <span>邮箱登录</span>
          <span class="tabline tabline-width">
      </span>
        </div>
      </div>
      <div class="mail-login" type="login">
        <div class="common-input">
          <img src="@/assets/mail-icon.svg" class="left-icon">
          <div class="input-view">
            <input placeholder="请输入注册邮箱" length="50" type="text" class="input">
            <p class="err-view">
            </p>
          </div>
          <img src="" class="right-icon" style="display: none;">
          <!---->
        </div>
        <div class="common-input">
          <img src="@/assets/pwd-icon.svg" class="left-icon">
          <div class="input-view">
            <input placeholder="请输入密码" length="24" type="password" class="input">
            <p class="err-view">
            </p>
          </div>
          <img src="@/assets/pwd-hidden.svg" class="right-icon">
          <!---->
        </div>
        <div class="next-btn-view">
          <button class="next-btn btn-active" style="margin: 16px 0px;">登录</button>
        </div>
        <div class="loading" style="display: none;">
          <div class="content tl-detail-loading">
          </div>
        </div>
      </div>
      <a href="/findPassword" class="forget-pwd" style="">忘记密码？</a>
    </div>
  </div>
</template>

<style scoped lang="less">
div {
  display: block;
}

.container {
  background-color: #24273a;
  height: 100%;
  max-width: 100%;
}

.new-content {
  position: absolute;
  left: 0;
  right: 0;
  margin: 80px auto 0;
  width: 980px;
}

.logo-img {
  width: 125px;
  display: block;
  margin-left: 137.5px;
}

.login-page {
  overflow: hidden;
  background: #fff;
  .logo-icon {
    margin-left: 175px;
  }
}

.pc-style {
  position: absolute;
  top: 74px;
  left: 100px;
  right: 0;
  width: 400px;
  height: 464px;
  background: #fff;
  border-radius: 4px;
}

.login-tab {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  color: #1e1e1e;
  font-size: 14px;
  height: 46px;
  line-height: 44px;
  margin-bottom: 40px;
  border-bottom: 1px solid #c3c9d5;

  div {
    position: relative;
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    text-align: center;
    cursor: pointer;
  }

  .tabline {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    margin: 0 auto;
    display: inline-block;
    width: 0;
    height: 2px;
    background: #3d5b96;
    -webkit-transition: width .5s cubic-bezier(.46, 1, .23, 1.52);
    transition: width .5s cubic-bezier(.46, 1, .23, 1.52);
  }

  tab-selected {
    color: #1e1e1e;
    font-weight: 500;
  }

  .mail-login, .tel-login {
    padding: 0 28px;
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

    err-view {
      margin-top: 4px;
      height: 16px;
      line-height: 16px;
      font-size: 12px;
      color: #f62a2a;
    }
  }
}

.btn-active {
  background: #3d5b96;
}

.next-btn {
  //background: #c3c9d5;
  border-radius: 4px;
  color: #fff;
  font-size: 14px;
  font-weight: 500;
  height: 40px;
  line-height: 40px;
  text-align: center;
  width: 100%;
  outline: none;
  cursor: pointer;
}

button {
  background: transparent;
  padding: 0;
  border-width: 0px;
}

button, input, select, textarea {
  margin: 0;
  padding: 0;
  outline: none;
}

.forget-pwd {
  text-align: center;
  display: block;
  width: 100px;
  overflow: hidden;
  white-space: nowrap;
  height: 36px;
  line-height: 36px;
  margin: 0 auto;
  color: #3d5b96;
  font-size: 12px;
  cursor: pointer;
}

</style>
