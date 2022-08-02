<template>
  <div>
    <leaf-82-search-bar></leaf-82-search-bar>
    <leaf-82-sell></leaf-82-sell>
    <leaf-82-buy></leaf-82-buy>
  </div>
</template>

<script>
import Leaf82SearchBar from '@/components/Leaf82SearchBar.vue'
import Leaf82Buy from '@/components/Leaf82Buy.vue'
import Leaf82Sell from '@/components/Leaf82Sell.vue'

export default {
  name: 'Leaf82View',
  components: {
    Leaf82SearchBar,
    Leaf82Buy,
    Leaf82Sell,
  },

}
</script>

<style>

</style>