<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import { mapActions } from 'vuex'


export default {
  name: 'App',
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

  body {
    background-color: #F8F5EE;
  }
</style>
