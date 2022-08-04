<template>
  <div class="leaf82-detail row">
    <!-- 여백 -->
    <div class="col-md-1 col-0"></div>
    <!-- 메인 -->
    <div class="main col-md-10 row py-5 my-5">
      <!-- 좌측 -->
      <div class="left col-md-5">
        <div class="img-box d-flex justify-content-center">
          <img :src="leaf82Detail.photo" alt="화분 사진">
        </div>
      </div>
      <!-- 우측 -->
      <div class="right col-md-7 mt-3 px-5">
        <div class="title d-flex justify-content-start py-1">
          <p>{ leaf82Detail.plantname } { leaf82Detail.category_class }</p>
        </div>
        <div class="username d-flex justify-content-start py-1">
          <p>{ leaf82Detail.user.nickname }</p>
        </div>
        <div class="price d-flex justify-content-start py-1">
          <p>{ leaf82Detail.price } 원</p>
        </div>
        <div class="addr d-flex justify-content-start py-1">
          <p>{ leaf82Detail.addr.sido } { leaf82Detail.addr.sigungu }</p>
        </div>
        <div class="status d-flex justify-content-start py-1">
          <p>{ leaf82Detail.status }</p>
        </div>
        <div class="content d-flex justify-content-start py-1">
          <p>{ leaf82Detail.content }</p>
        </div>
        <div class="btns d-flex justify-content-start py-3">
          <div class="message">
            <router-link :to="{ name : 'leaf82' }" class="d-flex justify-content-start">
              <button>채팅하러 가기</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <!-- 여백 -->
    <div class="col-md-1 col-0"></div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Leaf82Detail',
  computed: {
    ...mapGetters(['leaf82Detail']),
  }
}
</script>

<style scoped>
div {
  margin: 0;
  padding: 0;
}

.main {
  background-color: white;
}

/* 왼쪽 */
.img-box img{
  height: 300px;
  width: 300px;
  border-radius: 1rem;
}

/* 오른쪽 */

.message {
  width: 100%;
}

.message a {
  width: 100%;
  text-decoration: none;
}
.message a button {
  width: 100%;
  background-color: white;
  border-radius: 0.5rem;
  color: gray;
  border-width: 1px;
  border-color: gray;
  font-size: 0.8rem;
}

button:hover {
  cursor: pointer;
}
</style>