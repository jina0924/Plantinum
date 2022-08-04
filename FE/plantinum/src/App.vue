<template>
  <div id="app">
    <!-- <nav-bar v-if="isLoggedIn"></nav-bar> -->
    <!-- <nav-bar></nav-bar> -->
    <router-view></router-view>
  </div>
</template>

<script>
// import NavBar from '@/components/NavBar.vue'
// import { mapGetters, mapActions } from 'vuex'
import { mapActions } from 'vuex'


export default {
  name: 'App',
  // components: { NavBar },
  // computed: {
  //   ...mapGetters(['currentUser', 'isLoggedIn',])
  // },
  methods: {
    ...mapActions(['fetchCurrentUser', 'fetchProfile'])
  },
  created () {
    this.fetchCurrentUser()
  }
}
</script>

<style>
  #app {
    font-family: 'SUIT';
  }
</style>
