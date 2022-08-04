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
                <button class="btn plant-info-btn" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal">계절별 식물 관리 정보</button>

                <!-- 모달 -->
                <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                      </div>
                      <div class="modal-body">
                        ...
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary">Save changes</button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <div class="special-manage-info" v-if="myplant.plant_info.specl_manage_info">
                <button class="btn plant-info-btn">특별 관리 정보</button>
              </div>
              <div class="otp">
                <div v-if="!myplant.is_connected">
                  <button class="btn plant-info-btn plant-info-btn-end">OTP 발급</button>
                </div>
                <div v-if="myplant.is_connected">
                  <button>화분 연결 끊기</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 식물 일지 부분 -->



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
    ...mapGetters(['myplant']),
    myplantCreatedAt() {
      return this.myplant.created_at.substr(0, 10)
    }
  },
  methods: {
    ...mapActions(['fetchMyplant'])
  },
  created() {
    this.fetchMyplant(this.$route.params.plantPk)
  }
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
  color: #65805D;
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


</style>