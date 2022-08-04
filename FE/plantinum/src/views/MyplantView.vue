<template>
  <div class="myplant">
    <nav-bar></nav-bar>
    <!-- 배경 화면 -->
    <div class="container my-0">
      <div class="banner-img">
      </div>
    </div>
    <!-- 리스트 -->
    <myplant-list :myplants='myplants'></myplant-list>
    <!-- 추가 버튼 (스티키 바텀) -->
    <div class="create-btn d-flex justify-content-end" v-if="mypage">
      <router-link class="add px-5 mx-5 pb-5" :to="{ name: 'myplantNew' }">
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
import NavBar from '@/components/NavBar.vue'



export default {
  name: 'MyplantView',
  data() {
    return {
      myplantUsername : '',
      mypage : false,
    }
  },
  components : {
    MyplantList,
    NavBar,
  },
  methods : {
    ...mapActions(['fetchMyplants']),
    isMypage() {
      if (this.currentUser.username === this.myplantUsername) {
        this.mypage = true
      }
    }
  },
  computed : {
    ...mapGetters(['myplants', 'currentUser', 'isLoggedIn'])
  },
  created() {
    this.mypage = false
    const payload = { username: this.$route.params.username }
    this.myplantUsername = payload.username
    this.fetchMyplants(payload)
    this.isMypage()
    console.log(this.currentUser)
    console.log(this.isLoggedIn)
  },
}
</script>

<style scoped>
.container {
  height: 50vh;
  /* height: 500px; */
  /* width: 100vw; */
  margin: 0;
  padding: 0;
  max-width: 1920px;
  /* max-height: 500px; */
}

.banner-img {
  background-image: url('../assets/MyplantView/banner_img-02.svg');
  height: 100%;
  width: 100%;
  margin: 0;
  background-repeat: repeat-x;
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
  font-size: 2rem;
  margin: 0;
  line-height: 2.5rem;
}

.btn{
  border-radius: 100%;
  height: 60px;
  width: 60px;
  background-color: #b2c9ab;
  color: white;
}
</style>