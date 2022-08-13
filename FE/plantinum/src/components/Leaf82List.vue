<template>
  <div class="leaf82-sell">
    <!-- 분양해요 활성화 -->
    <div class="title d-flex justify-content-center mb-5" v-if="isSell">
      <span class="sell-on pr-2">분양해요</span>
      <span class="divider"> | </span>
      <span class="buy-off pl-2" @click="onoff()">분양받아요</span>
    </div>
    <!-- 분양해요 목록들 -->
    <div class="leaf82-list-box row pb-5" v-if="isSell">
      <div class="col-sm-2 col-md-3 col-0" v-if="!!sellItems"></div>
      <!-- 리스트가 있을 때 -->
      <div class="leaf82-list col-sm-8 col-md-6 col-0 row d-flex justify-content-center" v-if="!!sellItems">
        <div class="item px-2 pb-2" v-for="leaf82 in sellItems" :key="leaf82.pk">
          <router-link class="route" :to="{ name: 'leaf82Detail', params: { username: leaf82.user.username , posting_addr: leaf82.posting_addr } }">
          <!-- <router-link class="route" :to="{ }"> -->
            <div class="item-img d-flex justify-content-center">
              <img :src="leaf82.photo" :alt="`${leaf82.plantname} 사진입니다.`">
            </div>
            <div class="item-info">
              <p class="name">{{ leaf82.plantname }}</p>
              <p class="price">{{ leaf82.price }} 원</p>
              <p class="addr">{{ leaf82.addr.sido }} {{ leaf82.addr.sigungu }}</p>
              <p class="message">채팅 15</p>
            </div>
          </router-link>
        </div>
      </div>
      <div class="col-sm-2 col-md-3 col-0" v-if="!!sellItems"></div>
      <!-- 리스트가 없을때 -->
      <div class="col-sm-2 col-md-3 col-0" v-if="!sellItems[0]"></div>
      <div class="leaf82-list col-sm-8 col-md-6 col-0 mt-5" v-if="!sellItems[0]">
        <div class="d-flex justify-content-center">
          <span class="material-symbols-outlined noplant-icon">macro_off</span>
        </div>
        <div class="noplant-text d-flex justify-content-center">
          <p>등록된 식물이 없습니다.</p>
        </div>
      </div>
      <div class="col-sm-2 col-md-3 col-0" v-if="!sellItems[0]"></div>
    </div>

    <!-- 분양받아요 활성화 -->
    <div class="title d-flex justify-content-center mb-5" v-if="!isSell">
      <span class="sell-off pr-2" @click="onoff()">분양해요</span>
      <span class="divider"> | </span>
      <span class="buy-on pl-2">분양받아요</span>
    </div>
    <!-- 분양받아요 목록들 -->
    <div class="leaf82-list-box row pb-5" v-if="!isSell">
      <div class="col-sm-2 col-md-3 col-0" v-if="!!buyItems"></div>
      <!-- 리스트가 있을 때 -->
      <div class="leaf82-list col-sm-8 col-md-6 col-0 row d-flex justify-content-center" v-if="!!buyItems">
        <div class="item px-2 pb-2" v-for="leaf82 in buyItems" :key="leaf82.pk">
          <router-link class="route" :to="{ name: 'leaf82Detail', params: { username: leaf82.user.username , posting_addr: leaf82.posting_addr } }">
          <!-- <router-link class="route" :to="{ }"> -->
            <div class="item-img d-flex justify-content-center">
              <img :src="leaf82.photo" :alt="`${leaf82.plantname} 사진입니다.`">
            </div>
            <div class="item-info">
              <p class="name">{{ leaf82.plantname }}</p>
              <p class="price">{{ leaf82.price }} 원</p>
              <p class="addr">{{ leaf82.addr.sido }} {{ leaf82.addr.sigungu }}</p>
              <p class="message">채팅 15</p>
            </div>
          </router-link>
        </div>
      </div>
      <div class="col-sm-2 col-md-3 col-0" v-if="!!buyItems"></div>
      <!-- 리스트가 없을때 -->
      <div class="col-sm-2 col-md-3 col-0" v-if="!buyItems[0]"></div>
      <div class="leaf82-list col-sm-8 col-md-6 col-0 mt-5" v-if="!buyItems[0]">
        <div class="d-flex justify-content-center">
          <span class="material-symbols-outlined noplant-icon">macro_off</span>
        </div>
        <div class="noplant-text d-flex justify-content-center">
          <p>등록된 식물이 없습니다.</p>
        </div>
      </div>
      <div class="col-sm-2 col-md-3 col-0" v-if="buyItems[0]"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Leaf82List',
  props: {
    sellItems: Array,
    buyItems: Array
  },
  data() {
    return {
      isSell: true,
    }
  },
  methods: {
    onoff() {
      this.isSell = !this.isSell
    },
  },
}
</script>

<style scoped>
div {
  margin: 0;
  padding: 0;
}

.title {
  font-size: 2rem;
}

.divider {
  font-weight: bold;  
}

.sell-on {
  font-weight: bold;
}

.buy-off {
  color: #7E7E7E;
}

.buy-off:hover {
  color: black;
  cursor: pointer;
}

.sell-off {
  color: #7E7E7E;
}

.sell-off:hover {
  color: black;
  cursor: pointer;  
}

.buy-on {
  font-weight: bold;
}

p {
  margin: 0;
}

.item img {
  width: 130px;
  height: 130px;
  object-fit: cover;
}

.item-info .name {
  font-size: 1rem;
}

.item-info .price {
  font-size: 0.8rem;
  font-weight: bold;
}

.item-info .addr {
  font-size: 0.8rem;
}

.item-info .message {
  font-size: 0.7rem;
  color: #A6A6A6;
}

.noplant-icon {
  color: #A6A6A6;
  font-size: 15rem;
}

.noplant-text {
  color: #A6A6A6;
  font-size: 1.2rem;
}

a {
  color: black;
  text-decoration: none;
}
</style>