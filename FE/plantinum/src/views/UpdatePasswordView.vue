<template>
  <div class="profile">
    <div class="row mx-0">
      <!-- 여백 -->
      <div class="col-md-3"></div>
      <!-- 내용 담을 흰 상자 -->
      <update-password-detail class="col-md-6 mb-5 pb-5 pt-5"></update-password-detail>
      <!-- 여백 -->
      <div class="col-md-3"></div>
    </div>
  </div>
</template>

<script>
import UpdatePasswordDetail from '@/components/UpdatePasswordDetail.vue'

export default {
  name: 'UpdatePasswordView',
  components : {
    UpdatePasswordDetail
  }
}
</script>

<style scoped>
.profile {
  background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)), url('@/assets/ProfileView/background_img.jpg');
  background-size: cover;
  height: 1000px;
}
</style>