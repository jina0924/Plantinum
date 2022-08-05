<template>
  <div class="detail-back">
    <nav-bar></nav-bar>
    <div class="container">
      <div class="plant-profile">
        <div class="profile-body row justify-content-center align-items-center">

          <div class="plant-profile-img">
            <img :src="myplant.photo" :alt="`${myplant.nickname} 사진`" class="myplant-img">
          </div>
          <div class="col-lg-7 plant-profile-info">
            <h2 class="myplant-nickname">{{ myplant.nickname }}</h2>
            <div class="myplant-data botanical-name">{{ myplant.plant_info.name }}</div>
            <div class="myplant-data row">
              <span class="col-lg-5 col-xl-4">토양 습도</span>
              <span class="col-lg-7 col-xl-8">{{ myplant.sensing.moisture_level }}</span>
            </div>
            <div class="myplant-data row">
              <span class="col-lg-5 col-xl-4">등록 날짜</span>
              <span class="col-lg-7 col-xl-8">{{ myplantCreatedAt }}</span>
            </div>
            <div class="myplant-data row">
              <span class="col-lg-5 col-xl-4">최근 관수 날짜</span>
              <span class="col-lg-7 col-xl-8">{{ myplant.sensing.last_watering }}</span>
            </div>
            <div class="row">

              <div class="seasonal-manage-info">
                <button class="btn plant-info-btn" type="button" @click="changeModal(1)">계절별 식물 관리 정보</button>
                <!-- 모달 -->
                <div class="black-bg" @click="close($event)" v-if="!!modal">
                  <myplant-modal :plantInfo="myplant.plant_info" :modal="modal" class="myplant-modal"></myplant-modal>
                </div>
              </div>
              
              <div class="special-manage-info" v-if="myplant.plant_info.specl_manage_info">
                <button class="btn plant-info-btn" @click="changeModal(2)">특별 관리 정보</button>
                <div class="black-bg" @click="close($event)" v-if="!!modal">
                  <myplant-modal :plantInfo="myplant.plant_info" :modal="modal" class="myplant-modal"></myplant-modal>
                </div>
              </div>

              <div class="otp">
                <div v-if="!myplant.otp_code">
                  <button @click="[fetchOTP(myplantPk), startTimer()]" class="btn plant-info-btn plant-info-btn-end">{{ isConnected }}</button>
                  <!-- <div class="black-bg" @click="close($event)" v-if="!!modal">
                    <myplant-modal :otpCode="myplant.otp_code" :modal="modal" class="myplant-modal"></myplant-modal>
                  </div> -->
                </div>
                <div v-if="!!myplant.otp_code">
                  <button class="btn plant-info-btn plant-info-btn-end">{{ isConnected }}</button>
                </div>
              </div>
            </div>
            <div v-if="!myplant.is_connected && !myplant.otp_code" class="supool-info d-flex align-items-center">
              <span class="material-symbols-outlined supool-icon">potted_plant</span>
              SuPool은 Plantinum에서 제작한 자동화 화분입니다
            </div>
            <div v-if="!myplant.is_connected && !!myplant.otp_code" class="otp-timer">
              <div>{{ myplant.otp_code }}</div>
              <div>{{ otpTimer }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 식물 일지 부분 -->
    <!-- 모달 부분 -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import NavBar from '@/components/NavBar.vue'
import MyplantModal from '@/components/MyplantModal.vue'

export default {
  name: 'MyplantDetailView',
  data() {
    return {
      myplantPk: this.$route.params.plantPk,
      modal: 0,
      otpTimer: 10,
    }
  },
  components: { NavBar, MyplantModal },
  computed: {
    ...mapGetters(['myplant', 'temp_OTP']),
    myplantCreatedAt() {
      return this.myplant.created_at.substr(0, 10)
    },
    isConnected() {
      // return this.myplant.otp_code ? 'SuPool 연결 끊기' : 'SuPool 연결'
      if (this.myplant.is_connected) { 
        return 'SuPool 연결 끊기'
      } else if (this.myplant.otp_code && this.myplant.is_connected === false) {
        return 'SuPool 연결중'
      } else {
        return 'SuPool 연결'
      }
  },
  // watch: {
  //   }
  },
  methods: {
    ...mapActions(['fetchMyplant', 'fetchOTP', 'resetOTP']),
    close(event) {
      if (event.target.classList.contains('black-bg') || event.target.classList.contains('modal-close-btn')) {
        this.modal = 0
      }
    },
    changeModal(num) {
      this.modal = num
    }, 
    startTimer() {
      this.otpTimer = 10
      const interval = setInterval(() => {
        this.fetchMyplant(this.$route.params.plantPk)
        this.otpTimer--
        if (this.otpTimer <= 0 && this.myplant.otp_code === null) {
          this.stopTimer(interval)
        }
      }, 1000)
      return interval},
    stopTimer(Timer) {
      clearInterval(Timer)
      this.otpTimer = 10
    }
  },
  created() {
    this.fetchMyplant(this.$route.params.plantPk)
  },
}
</script>

<style scpoed>
body {
  background-color: #F8F5EE;
}

.profile-body { 
  background-color: white;
  border-radius: 15px;
  padding: 2.5rem;
}

.plant-profile-img {
  width: 20rem;
  height: 20rem;
  border-radius: 100%;
  overflow: hidden;
}

.myplant-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.plant-profile-info {
  padding: 0 0 0 5rem;
}

.myplant-nickname {
  font-size: 3.5rem;
  font-weight: 600;
}

.botanical-name {
  color: #b2c9ab;
  font-family: 'MaruBuri';
  font-size: 1.1rem;
  font-style: italic;
}

.myplant-data {
  line-height: 2rem;
  font-size: 1.1rem;
}

.plant-info-btn {
  margin: 0.5rem;
  padding: 0 1rem;
  border-radius: 13px;
  height: 45px;
  font-size: 1rem;
  background-color: white;
  color: #a6a6a6;
  border-color: #a6a6a6;
  border-style: solid;
  border-width: thin;
}

.plant-info-btn-end {
  margin: 0.5rem 0 0.5rem 0.5rem;
  color: #845A49;
  border-color: #845A49;
}

.black-bg {
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
  position: fixed;
  top: 0px;
  left: 0px;
}

.myplant-modal {
  position: relative;
  top: 150px;
}

.supool-info {
  font-size: 0.9rem;
  color: #845A49;
  margin-top: 0.7rem;
}

.supool-icon {
  margin-right: 0.7rem;
}
</style>