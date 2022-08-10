<template>
  <div class="edit-myplant">
    <nav-bar></nav-bar>
    <myplant-form :myplant="myplant" action="update"></myplant-form>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import MyplantForm from '@/components/MyplantForm.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MyplantEdit',
  components: { NavBar, MyplantForm },
  computed: {
    ...mapGetters(['myplant'])
  },
  methos: {
    ...mapActions(['fetchMyplant'])
  },
  created() {
    this.fetchMyplant(this.$route.params.plankPk)
  }
}
</script>

<style scoped>
.edit-myplant{  
  background-color: #F8F5EE;
}
</style>