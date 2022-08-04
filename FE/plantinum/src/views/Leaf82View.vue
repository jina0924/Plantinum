<template>
  <div>
    <nav-bar></nav-bar>
    <leaf-82-search-bar></leaf-82-search-bar>
    <leaf-82-list></leaf-82-list>
  </div>
</template>

<script>
import Leaf82SearchBar from '@/components/Leaf82SearchBar.vue'
import Leaf82List from '@/components/Leaf82List.vue'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'Leaf82View',
  components: {
    NavBar,
    Leaf82SearchBar,
    Leaf82List,
  },

}
</script>

<style scoped>
div {
  background-color: #F8F5EE;
}
</style>