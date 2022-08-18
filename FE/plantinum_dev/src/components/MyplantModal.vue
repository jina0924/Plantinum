<template>
  <div class="modal-bg">
    <div v-if="modal===1">
      <h5>계절별 식물 관리 정보</h5>
      <div class="season">봄</div>{{ plantInfo.watercycle_spring_nm }}
      <div class="season">여름</div>{{ plantInfo.watercycle_summer_nm }}
      <div class="season">가을</div>{{ plantInfo.watercycle_autumn_nm }}
      <div class="season">겨울</div>{{ plantInfo.watercycle_winter_nm }}
    </div>
    <div v-if="modal===2">
      <h5>특별 관리 정보</h5>
      <p>{{ plantInfo.specl_manage_info }}</p>
    </div>
    <!-- <div v-if="modal===3">
      <h5>화분 연결 OTP</h5>
      <p>{{ otpCode }}</p>
    </div> -->
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
    },
  }
}
</script>

<style scoped>
.modal-bg {
  width: 80vw;
  max-width: 450px;
  margin: 2rem auto;
  background: white ;
  border-radius: 15px;
  padding: 2rem 2rem 1rem 2rem;
}

h5 {
  text-align: center;
}

.season { 
  font-weight: 500;
  font-size: 1.1rem;
  color: #845A49;
  margin: 0.5rem 0;
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
  margin-left: auto;
  display: block;
  margin-top: 1.5rem;
}

.modal-close-btn:hover {
  background-color: #65805d;
  /* transform: scale(1.1); */
  transition: all 0.5s;
}

</style>