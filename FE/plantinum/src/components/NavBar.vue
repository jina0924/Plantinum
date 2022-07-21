<template>
  <nav class="navbar navbar-expand-lg navbar-light">
    <router-link class="navbar-brand" :to="{ name: 'home'}">Plantinum</router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <router-link class="nav-link" :to="{ name: 'myplant'}">내 식물</router-link>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            잎팔이
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <router-link class="dropdown-item" :to="{ name: 'leaf82' }">매물보기</router-link>
            <div class="dropdown-divider"></div>
            <router-link class="dropdown-item" :to="{ name: 'messenger' }">채팅</router-link>
          </div>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'profile'}">프로필</router-link>
        </li>
      </ul>
      <div class="nav-logout my-2 my-lg-0">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link class="nav-link" :to="{ name: 'logout'}" @click="fetchProfile()">Logout</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import {mapActions, mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  data() {

  },
  computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
    },
  methods : {
      ...mapActions(['fetchProfile']),
      movieSearch : function (searchMovie) {
        this.$router.push( {name : 'search', query: { searchMovie } }  )
        this.searchMovie = ''
      }
    },
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

  .navbar {
    background-color: #F8F5EE;
  }

  .nav-logout .nav-item {
    background-color: #B2C9AB;
    font-family: 'SUIT', sans-serif;
    border-radius: 10px;
    font-size: 0.5rem;
    /* 컬러가 안먹어 ㅠㅠㅠ */
    color: white;
  }

  /* 드랍다운 CSS */

</style>