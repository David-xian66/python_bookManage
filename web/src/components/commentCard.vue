<template>
  <div class="comments-wrapper">
    <div class="clearfix Comments-hd">
      <h2>
        <span>短评</span>&nbsp;·&nbsp;·&nbsp;·&nbsp;·&nbsp;·&nbsp;·
        <span class="pl">&nbsp;(<a href="">共 1498 条</a>)</span>
      </h2>
    </div>
    <div class="title_line clearfix color_gray">
      <div class="fleft Comments-sortby">
        <span>热门</span>
        <a href="">最新</a>
      </div>
    </div>
    <div id="comments">
      <div class="comment-list score " id="">
        <ul>
          <template v-for="item in commentData">
            <li class="comment-item" data-cid="3505217667">
              <div class="avatar">
            <span>
              <a-avatar :size="48" icon="user" src="https://img2.doubanio.com/icon/u1655518-111.jpg"/>
            </span>
              </div>
              <div class="comment">
                <h3>
                  <span class="comment-vote">
                    <a-icon type="like"/>
                    <a id="btn-3505217667" href="" class="j vote-comment">赞</a>
                  </span>
                  <span class="comment-info">
                    <a href="">艾莉森王</a>
                    <span class="comment-time" href="">2022-09-21 15:24:11</span>
                    <span class="comment-location">德国</span>
                  </span>
                </h3>
                <p class="comment-content">
                  <span class="short">喜欢直面死亡的主题，不仅仅是海德格尔式向死而生，而是“像成熟的果子自然从树上掉下”，死的时候，人和世间都没有伤口！</span>
                </p>
              </div>
            </li>
          </template>
        </ul>
      </div>
      <div class="paginator-wrapper">
        <a-pagination size="small" :total="50"/>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'CommentCard',
  data() {
    return {
      commentData: ['1', '1', '1', '1', '1', '1']
    }
  }
}
</script>
<style src="@/style/index/index.less" scoped lang="less"></style>
<style scoped>
h2 {
  color: #007722;
  border-bottom: 0px solid #ddd;
}

.paginator-wrapper {
  text-align: center;
}

</style>
