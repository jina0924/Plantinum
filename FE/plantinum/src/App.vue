<template>
  <div id="app">
    <!-- <nav-bar v-if="isLoggedIn"></nav-bar> -->
    <nav-bar></nav-bar>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import { mapActions, mapGetters } from 'vuex'


export default {
  name: 'App',
  components: { NavBar },
  methods: {
      ...mapActions(['fetchCurrentUser',])
    },
    computed: {
      ...mapGetters(['currentUser', 'isLoggedIn',])
    },
    created(){
      this.fetchCurrentUser()

    },
}
</script>

<style>
</style>
