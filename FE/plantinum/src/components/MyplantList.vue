<template>
  <div>
    <!-- 리스트가 있을 때 -->
    <div class="yesplant row" v-if="myplant[0]">
      <div class="col-md-2 px-0"></div>
      <div class="col-md-8 col-sm-12 row px-0 mx-0">
        <div class="card mt-2 col-md-3 col-sm-6 px-0" v-for="plant in myplant" :key="plant.id">
          <div class="plant-img d-flex justify-content-center">
            <img :src="`${plant.photo}`" :alt="`${plant.nickanme} 사진 입니다.`">
          </div>
          <div class="d-flex justify-content-between">
            <div class="col-6">
              <span class="plant-info">
                {{ plant.nickname }}
              </span>
            </div>
            <div class="col-6 d-flex justify-content-end align-items-center">
              <span class="material-symbols-outlined humidity">water_drop</span>
              <span class="humidity">{{ plant.습도 }} %</span>
              <span class="material-symbols-outlined diary-count">description</span>
              <span class="diary-count">{{ plant.일지수 }}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-2 px-0"></div>
    </div>
    <!-- 리스트가 없을 때 -->
    <div class="container">
      <div class="noplant" v-if="!myplant[0]">
        <span class="material-symbols-outlined">
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
  padding-left: 1rem;
  padding-right: 1rem;
}

.plant-img img {
  width: 95%;
  height: 95%;
}

.plant-info {
  font-size: 1rem;
}

.diary-count {
  font-size: 0.5rem;
  color: #A17C6B;
}

.humidity {
  font-size: 0.5rem;
  color: #18A7DB;
}

.material-symbols-outlined {
  font-size: 13rem;
  margin: 0 0 1rem 0;
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