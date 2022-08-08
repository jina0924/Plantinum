<template>
  <div class="new-myplant">
    <nav-bar></nav-bar>
    <myplant-form :myplant="myplant" action="create"></myplant-form>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import MyplantForm from '@/components/MyplantForm.vue'
// import PlantSearchBar from '@/components/PlantSearchBar.vue'

export default {
  name: 'MyplantNewView',
  // components: { NavBar, MyplantForm, PlantSearchBar },
  components: { NavBar, MyplantForm },
  data() {
    return {
      myplant: {
        nickname: '',
        photo: 'https://url.kr/d1acln',
        name_id: '',
      }
    }
  }
}
</script>

<style scoped>
.new-myplant{
  background-color: #F8F5EE;
}
</style>