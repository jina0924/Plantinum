<template>
  <nav class="navbar navbar-expand-lg navbar-light px-5">
    <router-link class="navbar-brand" :to="{ name: 'home'}">Plantinum</router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item" v-if="isLoggedIn">
          <!-- <router-link class="nav-link pb-0 mx-2" :to="{ name: 'login' }" v-if="!isLoggedIn">내 식물</router-link> -->
          <!-- <router-link class="nav-link pb-0 mx-2" :to="{ name: 'myplant', params: { username } }" v-if="isLoggedIn">내 식물</router-link> -->
          <router-link class="nav-link pb-0 mx-2" :to="{ name: 'myplant', params: { username } }">내 식물</router-link>
        </li>
        <li class="nav-item" v-if="!isLoggedIn">
          <router-link class="nav-link pb-0 mx-2" :to="{ name: 'login' }">내 식물</router-link>
          <!-- <router-link class="nav-link pb-0 mx-2" :to="{ name: 'myplant', params: { username } }" v-if="isLoggedIn">내 식물</router-link> -->
          <!-- <router-link class="nav-link pb-0 mx-2" :to="{ name: 'myplant', params: { username } }" v-if="!!username">내 식물</router-link> -->
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle pb-0 mx-2" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            잎팔이
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <router-link class="dropdown-item" :to="{ name: 'leaf82' }">거래</router-link>
            <div class="dropdown-divider"></div>
            <router-link class="dropdown-item" :to="{ name: 'messenger' }" v-if="isLoggedIn">채팅</router-link>
            <router-link class="dropdown-item" :to="{ name: 'login' }" v-if="!isLoggedIn">채팅</router-link>
          </div>
        </li>
        <li class="nav-item">
          <router-link class="nav-link pb-0 mx-2" :to="{ name: 'profile' }" v-if="isLoggedIn">프로필</router-link>
          <router-link class="nav-link pb-0 mx-2" :to="{ name: 'login' }" v-if="!isLoggedIn">프로필</router-link>          
        </li>
      </ul>
      <div class="my-2 my-lg-0">
        <!-- <router-link class="nav-link" :to="{ }" @click="logout" v-if="isLoggedIn">
          <button class="btn">로그아웃</button>
        </router-link> -->
        <button class="btn nav-link" @click="logout" v-if="isLoggedIn">로그아웃</button>
        <router-link class="nav-link" :to="{ name: 'login' }" v-if="!isLoggedIn">
          <button class="btn">로그인</button>
        </router-link>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'NavBar',
  // data() {
  //   return {
  //     username : 'guest'
  //   }
  // },
  computed: {
    ...mapGetters(['isLoggedIn', 'username']),
    // username() {
    //   return this.currentUser.username
    // }
  },
  methods: {
    ...mapActions(['logout',]),
    // abc () {
    //   this.username = this.currentUser.username
    // }
  },
  // created () {
    // console.log(this.currentUser)
    // this.abc()
  // }
}
</script>

<style scoped>
  .navbar-brand {
    font-family: 'Dancing Script', cursive;
    font-size: 2.5rem;
  }

  .nav-link {
    font-family: 'SUIT', sans-serif;
  }

  .dropdown-item {
    font-family: 'SUIT', sans-serif;
  }

  .btn{
    border-radius: 5px;
    height: 44px;
    font-size: 1rem;
    background-color: #b2c9ab;
    color: white;
    width: 100%;
  }

  /* .nav-item a.router-link-exact-active {
  font-weight: 600px;
  text-align: center;
  text-decoration-line: none;
} */

</style>