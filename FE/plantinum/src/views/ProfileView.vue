<template>
  <div>
    <div class="profile row">
      <!-- 여백 -->
      <div class="col-md-1"></div>
      <!-- 내용 담을 흰 상자 -->
      <profile-detail class="col-md-10 mb-5 pb-5"></profile-detail>
      <!-- 여백 -->
      <div class="col-md-1"></div>
    </div>
  </div>
</template>

<script>
import ProfileDetail from '@/components/ProfileDetail.vue'

export default {
  name: 'ProfileView',
  components: {
    ProfileDetail
  }
}
</script>

<style scoped>
.profile {
  background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)), url('@/assets/ProfileView/background_img.jpg');
  background-size: cover;
}
</style>
