<template>
  <div class="leaf82-sell">
    <!-- 분양해요 활성화 -->
    <div class="title d-flex justify-content-center mb-5" v-if="isSell">
      <span class="sell-on">분양해요</span>
      <span class="divider">|</span>
      <span class="buy-off" @click="onoff()">분양받아요</span>
    </div>
    <!-- 분양해요 목록들 -->
    <div class="leaf82-list-box row mb-5" v-if="isSell">
      <div class="col-sm-2 col-md-3 col-0" v-if="!!sellItems"></div>
      <!-- 리스트가 있을 때 -->
      <div class="leaf82-list col-sm-8 col-md-6 col-0 row d-flex justify-content-center" v-if="!!sellItems">
        <div class="item px-2 pb-2" v-for="leaf82 in sellItems" :key="leaf82.pk">
          <!-- <router-link class="route" :to="{ name: 'leaf82Detail', params: { username: leaf82.user.username , posting_addr: leaf82.posting_addr } }"> -->
          <router-link class="route" :to="{ }">
            <div class="item-img d-flex justify-content-center">
              <img src="data:image/jpeg;base64,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" alt="">
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
      <span class="sell-off" @click="onoff()">분양해요</span>
      <span class="divider">|</span>
      <span class="buy-on">분양받아요</span>
    </div>
    <!-- 분양받아요 목록들 -->
    <div class="leaf82-list-box row mb-5" v-if="!isSell">
      <div class="col-sm-2 col-md-3 col-0" v-if="!!buyItems"></div>
      <!-- 리스트가 있을 때 -->
      <div class="leaf82-list col-sm-8 col-md-6 col-0 row d-flex justify-content-center" v-if="!!buyItems">
        <div class="item px-2 pb-2" v-for="leaf82 in buyItems" :key="leaf82.pk">
          <!-- <router-link class="route" :to="{ name: 'leaf82Detail', params: { username: leaf82.user.username , posting_addr: leaf82.posting_addr } }"> -->
          <router-link class="route" :to="{ }">
            <div class="item-img d-flex justify-content-center">
              <img src="data:image/jpeg;base64,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" alt="">
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
  color: #7E7E7E;
}

.noplant-icon {
  color: #7E7E7E;
}

.noplant-text {
  color: #7E7E7E;
  font-size: 0.9rem;
}

a {
  color: black;
  text-decoration: none;
}
</style>