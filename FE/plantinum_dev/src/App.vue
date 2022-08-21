<template>
  <div id="app">
    <!-- <nav-bar v-if="isLoggedIn"></nav-bar> -->
    <!-- <nav-bar></nav-bar> -->
    <router-view></router-view>
    <footer-bar></footer-bar>

  </div>
</template>

<script>
// import NavBar from '@/components/NavBar.vue'
// import { mapGetters, mapActions } from 'vuex'
import { mapActions } from 'vuex'
import FooterBar from '@/components/FooterBar.vue'



export default {
  name: 'App',
  components: { FooterBar },
  // computed: {
  //   ...mapGetters(['currentUser', 'isLoggedIn',])
  // },
  data() {
    return {
      viewWidth: window.innerWidth
    }
  },
  methods: {
    ...mapActions(['fetchCurrentUser', 'fetchProfile', 'setDevice', 'getDevice']),
    // 너비가 변할 때 넘겨줄 데이터
    handleResize() {
      this.viewWidth = window.innerWidth
    },    
  },
  mounted() {
    window.addEventListener('resize', this.handleResize);
	},
  beforeUnmount() {
    window.removeEventListener('resize', this.handleResize);
  },
  created () {
    this.fetchCurrentUser()
    this.getDevice()
  },
  watch: {
    viewWidth() {
      this.setDevice(this.viewWidth)
    }
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
