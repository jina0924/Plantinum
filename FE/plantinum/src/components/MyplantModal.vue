<template>
  <div class="modal-bg">
    <div v-if="modal===1">
      <p>봄 : {{ plantInfo.watercycle_spring_nm }}</p>
      <p>여름 : {{ plantInfo.watercycle_summer_nm }}</p>
      <p>가을 : {{ plantInfo.watercycle_autumn_nm }}</p>
      <p>겨울 : {{ plantInfo.watercycle_winter_nm }}</p>
    </div>
    <div v-if="modal===2">
      <p>{{ plantInfo.specl_manage_info }}</p>
    </div>
    <button class="modal-close-btn">닫기</button>
  </div>
</template>

<script>
export default {
  name: 'MyplantModal',
  props: {
    plantInfo: {
      type: Object
    },
    modal: {
      type: Number
    }
  }
}
</script>

<style scoped>
.modal-bg {
  width: fit-content;
  margin: 2rem auto;
  background: white ;
  border-radius: 15px;
  padding: 2rem;
}

.modal-close-btn {
  cursor: pointer;
  border: none;
  background-color: #b2c9ab;
  color: white;
  font-weight: 500;
  margin: 0.5rem;
  padding: 0 1rem;
  border-radius: 13px;
  height: 45px;
  font-size: 1rem;
}

.modal-close-btn:hover {
  background-color: #65805d;
  /* transform: scale(1.1); */
  transition: all 0.5s;
}

</style>