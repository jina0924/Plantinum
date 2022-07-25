<template>
  <div class="detail-back">
    <div class="plant-profile">
      <div class="col-4 plant-profile-img">사진</div>
      <div class="col-8 plant-profile-info">정보</div>
    </div>
    <hr>
    <p>식물일지</p>
    <div class="plant-diary-list">
      <div class="col-3 card">일지 사진</div>
    </div>
    <hr>


  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: MyplantDetailView,
  data() {
    return {
      
    }
  }
}
</script>

<style scpoed>

</style>