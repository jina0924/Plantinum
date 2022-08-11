<template>
  <div class="messenger">
    <nav-bar></nav-bar>
    <messenger-list></messenger-list>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import MessengerList from '@/components/MessengerList.vue'

export default {
  name: 'MessengerView',
  components: {
    NavBar,
    MessengerList
  }
}
</script>

<style scoped>
.messenger {
  background-color: #F8F5EE;
}
</style>