<template>
  <div id="app">
    <!-- <nav-bar v-if="isLoggedIn"></nav-bar> -->
    <nav-bar></nav-bar>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import { mapGetters } from 'vuex'


export default {
  name: 'App',
  components: { NavBar },
  computed: {
    ...mapGetters(['currentUser', 'isLoggedIn',])
  },
}
</script>

<style>
  #app {
    font-family: 'SUIT';
  }
</style>
