<template>
  <div class="myplant">
    <!-- 배경 화면 -->
    <div class="banner">
    </div>
    <!-- 리스트 -->
    <myplant-list :myplant='myplant'></myplant-list>
    <!-- 추가 버튼 (스티키 바텀) -->
    <div class="create-btn d-flex justify-content-end" v-if="mypage">
      <router-link class="add px-5 mx-5 pb-5" :to="{  }">
        <button class="btn">
          <span class="material-symbols-outlined">add</span>
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MyplantList from '@/components/MyplantList.vue'

export default {
  name: 'MyplantView',
  data() {
    return {
      myplantNickname : '',
      mypage : false,
    }
  },
  components : {
    MyplantList,
  },
  methods : {
    ...mapActions([
      'setMyplant',
      ]),
    isMypage() {
      if (this.currentUser.usernickname === this.myplantNickname) {
        this.mypage = true
      }
    }
  },
  computed : {
    ...mapGetters([
      'myplant',
      'currentUser'
    ])
  },
  created() {
    this.mypage = false
    const payload = { usernickname: this.$route.params.usernickname}
    this.myplantNickname = payload.usernickname
    this.setMyplant(payload)
    this.isMypage()
  }

}
</script>

<style scoped>
.banner {
  background-image: url('../assets/MyplantView/banner_img-01.jpg');
  height: 600px;
  background-size: cover;  
}

.myplant {
  background-color: #F8F5EE;
}

.a {
  text-decoration: none;
}

.material-symbols-outlined {
  color: white;
  font-weight: bold;
  font-size: 1rem;
}

.btn{
  border-radius: 100%;
  height: 44px;
  font-size: 1rem;
  background-color: #b2c9ab;
  color: white;
  width: 100%;
}
</style>