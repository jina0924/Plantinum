<template>
  <div class="leaf82-detail-view">
    <leaf-82-detail></leaf-82-detail>
  </div>
</template>

<script>
import Leaf82Detail from '@/components/Leaf82Detail.vue'
import { mapActions } from 'vuex'

export default {
  name: 'Leaf82DetailView',
  components: {
    Leaf82Detail
  },
  methods: {
    ...mapActions(['fetchLeaf82Detail'])
  },
  created() {
    this.fetchLeaf82Detail()
  }
}
</script>

<style>

</style>