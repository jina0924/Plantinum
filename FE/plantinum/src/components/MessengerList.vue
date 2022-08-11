<template>
  <div class="messenger-list py-5 row">
    <!-- 여백 -->
    <div class="col-md-2 col-0"></div>

    <!-- 채팅 박스 -->
    <div class="list-box col-md-8 col-12 row">
      <!-- 좌측 리스트 -->
      <div class="list col-md-6">

      </div>
      <!-- 우측 채팅방선택 안내 -->
      <div class="notification col-6">
        채팅방을 선택해주세요
      </div>
    </div>

    <!-- 여백 -->
    <div class="col-md-2 col-0"></div>
  </div>
</template>

<script>
export default {
  name: 'MessengerList'
}
</script>

<style scoped>
.messenger-list {
  height: 100%;
}

div {
  margin: 0;
  padding: 0;
}

.list-box{
  background-color: white;
  background-size: cover;
  border-radius: 0.5rem;
  height: 40rem;
}

.list {
  border-right: 1px solid;
  border-color: rgb(185, 185, 185);
}

</style>