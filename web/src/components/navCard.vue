<template>
  <div>
    <div id="db-global-nav" class="global-nav">
      <div class="bd">

        <div class="top-nav-info">
          <a href="#" class="nav-login" rel="nofollow">登录/注册</a>
        </div>

        <div class="top-nav-doubanapp">
          <a href="#" class="lnk-doubanapp">后台管理</a>
        </div>

        <div class="global-nav-items">
          <ul>
            <li class="">
              <a href="#" target="_blank">公告：该页面属于图书管理系统前台演示页面~</a>
            </li>
          </ul>
        </div>

      </div>
    </div>
    <div id="db-nav-book" class="nav">
      <div class="nav-wrap">
        <div class="nav-primary">
          <div class="nav-logo">
            <a href="#">Face读书</a>
          </div>
          <div class="nav-search">
            <form>
              <fieldset>
                <legend>搜索：</legend>
                <label for="inp-query">
                </label>
                <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="书名、作者、ISBN"
                                        value="" autocomplete="off"></div>
                <div class="inp-btn"><input type="submit" value="搜索"></div>
                <input type="hidden" name="cat" value="1001">
              </fieldset>
            </form>
          </div>
        </div>

      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'NavCard'
}
</script>
<style src="@/style/index/index.less" scoped lang="less"></style>
<style scoped lang="less">

.login {
  position: absolute;
  right: 30px;
  bottom:24px;
}
</style>
