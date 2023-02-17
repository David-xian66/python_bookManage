<template>
  <div data-v-1b2faf0e="" class="mine-infos-view">
    <div class="info-box flex-view">
      <img src="@/assets/avatar.jpg" alt="sdhh_3381" class="avatar-img">
      <div class="name-box">
        <h2 class="nick">sdhh_3381</h2>
        <div class="age">
          <span>活跃1天</span>
          <span class="give-point">个人主页</span>
        </div>
      </div>
    </div>
    <div class="counts-view">
      <div class="counts flex-view">
        <div class="fans-box flex-item" @click="clickMenu('collectBookView')">
          <div class="text">收藏</div>
          <div class="num">0</div>
        </div>
        <div class="split-line">
        </div>
        <div class="follow-box flex-item" @click="clickMenu('wishBookView')">
          <div class="text">心愿单</div>
          <div class="num">2</div>
        </div>
        <div class="split-line">
        </div>
        <div class="points-box flex-item">
          <div class="text">积分</div>
          <div class="num">0</div>
        </div>
      </div>
    </div>
    <div class="order-box">
      <div class="title">借阅中心</div>
      <div class="list">
        <div class="mine-item flex-view" @click="clickMenu('borrowView')">
          <img src="@/assets/order-icon.svg">
          <span>我的借阅</span>
        </div>
        <div class="mine-item flex-view" @click="clickMenu('orderView')">
          <img src="@/assets/order-icon.svg" alt="我的订单">
          <span>我的订单</span>
        </div>
        <div class="mine-item flex-view" @click="clickMenu('commentView')">
          <img src="@/assets/order-book-icon.svg" alt="我的评论">
          <span>我的评论</span>
        </div>
        <div class="mine-item flex-view" @click="clickMenu('addressView')">
          <img src="@/assets/order-address-icon.svg" alt="地址管理">
          <span>地址管理</span>
        </div>
        <div class="mine-item flex-view" @click="clickMenu('')">
          <img src="@/assets/order-point-icon.svg" alt="我的银子">
          <span>我的银子</span>
        </div>
      </div>
    </div>
    <div class="setting-box">
      <div class="title">个人设置</div>
      <div class="list">
        <div class="mine-item flex-view" @click="clickMenu('userInfoEditView')">
          <img src="@/assets/setting-icon.svg" alt="编辑资料">
          <span>编辑资料</span>
        </div>
        <div class="mine-item flex-view" @click="clickMenu('securityView')">
          <img src="@/assets/setting-safe-icon.svg" alt="账号安全">
          <span>账号安全</span>
        </div>
        <div class="mine-item flex-view" @click="clickMenu('pushView')">
          <img src="@/assets/setting-push-icon.svg" alt="推送设置">
          <span>推送设置</span>
        </div>
        <div class="mine-item flex-view" @click="clickMenu('messageView')">
          <img src="@/assets/setting-msg-icon.svg" alt="消息管理">
          <span>消息管理</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MineInfosView',
  methods: {
    clickMenu (name) {
      console.log('mmmmm')
      this.$router.push({name: name})
    }
  }
}
</script>

<style scoped lang="less">
.flex-view {
  display: flex;
}

.mine-infos-view {
  width: 235px;
  margin-right: 20px;
  border: 1px solid #cedce4;
  height: fit-content;

  .info-box {
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    padding: 16px 16px 0;
    overflow: hidden;
  }

  .avatar-img {
    width: 48px;
    height: 48px;
    margin-right: 16px;
    border-radius: 50%;
  }

  .name-box {
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    overflow: hidden;

    .nick {
      color: #152844;
      font-weight: 600;
      font-size: 18px;
      line-height: 24px;
      height: 24px;
      text-overflow: ellipsis;
      white-space: nowrap;
      margin: 0;
      overflow: hidden;
    }

    .age {
      font-size: 12px;
      color: #6f6f6f;
      height: 16px;
      line-height: 16px;
      margin-top: 8px;
    }

    .give-point {
      color: #4684e2;
      cursor: pointer;
      float: right;
    }
  }

  .counts-view {
    border: none;
    padding: 16px;
  }

  .counts {
    margin-top: 12px;
    text-align: center;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;

    .flex-item {
      -webkit-box-flex: 1;
      -ms-flex: 1;
      flex: 1;
      cursor: pointer;
    }

    .text {
      height: 16px;
      line-height: 16px;
      color: #6f6f6f;
    }

    .num {
      height: 18px;
      line-height: 18px;
      color: #152844;
      font-weight: 600;
      font-size: 14px;
      margin-top: 4px;
    }

    .split-line {
      width: 1px;
      height: 24px;
      background: #dae6f9;
    }
  }

  .intro-box {
    border-top: 1px solid #cedce4;
    padding: 16px;

    .title {
      color: #6f6f6f;
      font-size: 12px;
      line-height: 16px;
    }

    .intro-content {
      color: #152844;
      font-size: 14px;
      line-height: 20px;
      overflow: hidden;
      text-overflow: ellipsis;
      margin: 8px 0;
    }
  }

  .create-box {
    cursor: pointer;
    border-top: 1px solid #cedce4;
    padding: 16px;

    .title {
      position: relative;
      color: #152844;
      font-weight: 600;
      font-size: 14px;
      line-height: 18px;
      height: 18px;
    }

    .counts {
      margin-top: 12px;
      text-align: center;
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;

      .flex-item {
        -webkit-box-flex: 1;
        -ms-flex: 1;
        flex: 1;
        cursor: pointer;
      }

      .split-line {
        width: 1px;
        height: 24px;
        background: #dae6f9;
      }
    }
  }

  .order-box {
    border-top: 1px solid #cedce4;
    padding: 16px;

    .title {
      color: #152844;
      font-weight: 600;
      font-size: 14px;
      line-height: 18px;
      height: 18px;
      margin-bottom: 8px;
    }

    .list {
      padding-left: 16px;

      .mine-item {
        border-top: 1px dashed #cedce4;
        cursor: pointer;
        height: 48px;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;

        img {
          width: 24px;
          margin-right: 8px;
          height: 24px;
        }

        span {
          color: #152844;
          font-size: 14px;
        }
      }

      .mine-item:first-child {
        border: none;
      }
    }
  }

  .setting-box {
    border-top: 1px solid #cedce4;
    padding: 16px;

    .title {
      color: #152844;
      font-weight: 600;
      font-size: 14px;
      line-height: 18px;
      height: 18px;
      margin-bottom: 8px;
    }

    .list {
      padding-left: 16px;
    }

    .mine-item {
      border-top: 1px dashed #cedce4;
      cursor: pointer;
      height: 48px;
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;

      img {
        width: 24px;
        margin-right: 8px;
        height: 24px;
      }

      span {
        color: #152844;
        font-size: 14px;
      }
    }

    .mine-item:first-child {
      border: none;
    }
  }
}
</style>
