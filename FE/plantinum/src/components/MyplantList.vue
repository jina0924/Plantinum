<template>
  <div>
    <!-- 리스트가 있을 때 -->
    <div class="yesplant row justify-content-center" v-if="myplant[0]">
      <!-- <div class="col-md-2 px-0"></div> -->
      <div class="col-10 row px-0 card-section justify-content-center">
        <div class="card my-2 px-0 mx-2" v-for="plant in myplant" :key="plant.id">
          <div class="plant-img d-flex">
            <img :src="`${plant.photo}`" :alt="`${plant.nickanme} 사진 입니다.`" class="img-fluid">
          </div>
          <div class="d-flex justify-content-between plant-info">
            <div class="col-8">
              <span class="plant-name">
                {{ plant.nickname }}
              </span>
            </div>
            <div class="col-4 d-flex justify-content-end align-items-center">
              <span class="material-symbols-outlined humidity">water_drop</span>
              <span class="humidity">{{ plant.습도 }} %</span>
              <!-- <span class="material-symbols-outlined diary-count">description</span>
              <span class="diary-count">{{ plant.일지수 }}</span> -->
            </div>
          </div>
        </div>
      </div>
      <!-- <div class="col-md-2 px-0"></div> -->
    </div>
    <!-- 리스트가 없을 때 -->
    <div class="container">
      <div class="noplant" v-if="!myplant[0]">
        <span class="material-symbols-outlined noplant-icon">
          macro_off
        </span>
        <p>등록된 식물이 없습니다.</p>
      </div>
    </div>
  </div>
</template>

<script scoped>
export default {
  name : 'MyplantList',
  props : {
    myplant: Array
  }
}
</script>

<style>
.yesplant {
  padding: 1rem 2rem;
}

/* .card-section {
  object-position: 50% 50%;
} */

.card {
  border-radius: 10px;
  border-style: none;
  width: 16rem;
}

.plant-img img {
  /* width: 95%;
  height: 95%; */
  width: 250px;
  height: 250px;
  padding: 0.5rem;
  border-radius: 20px;
}

.plant-info {
  font-size: 1rem;
  margin: 1rem 0;
}

.diary-count {
  font-size: 0.5rem;
  color: #A17C6B;
}

.humidity {
  font-size: 1rem;
  color: #18A7DB;
}

.material-symbols-outlined {
  font-size: 1.5rem;
  /* margin: 0 0 1rem 0; */
}

.noplant-icon {
  font-size: 14rem;
  /* margin: 0 0 1rem 0; */
}

.container {
  margin: 3rem auto;
}

.noplant {
  color: #A6A6A6;
  margin: 5rem, auto;
  text-align: center;
  font-size: 1.5rem;
}
</style>