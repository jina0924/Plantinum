<template>
  <div class="detail-back">
    <nav-bar></nav-bar>
    <div class="plant-profile">
      <div class="col-4 plant-profile-img">사진</div>
      <div class="col-8 plant-profile-info">정보</div>
    </div>
    <!-- 식물 일지 부분 -->
    <!-- <hr>
    <p>식물일지</p>
    <div class="plant-diary-list">
      <div class="col-3 card">일지 사진</div>
    </div> -->
    <hr>


  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'MyplantDetailView',
  data() {
    return {
      myplantPk: this.$route.params.plantPk
    }
  },
  components: { NavBar },
  computed: {
    ...mapGetters(['myplant'])
  },
  methods: {
    ...mapActions(['fetchMyplant'])
  },
  created() {
    this.fetchMyplant(this.myplantPk)
  }
}
</script>

<style scpoed>
.detail-back {
  background-color: #F8F5EE;
}
</style>