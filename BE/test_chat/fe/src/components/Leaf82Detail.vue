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
        <!-- <div class="update row d-flex justify-content-center"> -->
        <div class="update row d-flex justify-content-center" v-if="this.$route.params.username === currentUser.username">
          <div class="update-box mx-3 my-2">
            <router-link class="update-a" :to="{ name: 'leaf82Edit' , params: { username: this.$route.params.username , posting_addr: this.$route.params.posting_addr } }">
              <button class="update-btn">수정</button>
            </router-link>
          </div>
          <div class="delete-box mx-3 my-2">
            <button class="delete-btn" @click="deleteLeaf82(deleteInfo)">삭제</button>
          </div>
        </div>
      </div>
      <!-- 우측 -->
      <div class="right col-md-7 mt-3 px-5">
        <div class="plantname d-flex justify-content-start">
          <p>{{ leaf82Detail.plantname }} {{ leaf82Detail.category_class }}</p>
        </div>
        <hr>
        <div class="nickname d-flex justify-content-start pb-1">
          <router-link :to="{ name: 'myplant' , params: { username: this.$route.params.username } }" class="nickname-route">
            <img :src="user.photo" :alt="`${ user.nickname }의 프로필 사진입니다.`" class="user-photo mr-1">
          </router-link>
          <router-link :to="{ name: 'myplant' , params: { username: this.$route.params.username } }" class="nickname-route">
            <p>{{ user.nickname }}</p>
          </router-link>
        </div>
        <div class="price d-flex justify-content-start pb-1">
          <p>{{ leaf82Detail.price }} 원</p>
        </div>
        <div class="addr d-flex justify-content-start pb-1">
          <p>{{ addr.sido }} {{ addr.sigungu }}</p>
        </div>
        <div class="status d-flex justify-content-start pb-1">
          <p>{{ leaf82Detail.status_class }}</p>
        </div>
        <div class="content d-flex justify-content-start py-1 my-3">
          <p>{{ leaf82Detail.content }}</p>
        </div>
        <div class="btns d-flex justify-content-center py-3" v-if="leaf82Detail.status_class === '판매중'">
          <div class="message" v-if="isLoggedIn">
            <router-link :to="{ name : 'messenger' }" class="d-flex justify-content-center" @click = "goChat()">
              <button class="py-2" >채팅하러 가기</button>
            </router-link>
          </div>
          <div class="message" v-if="!isLoggedIn">
            <router-link :to="{}" class="d-flex justify-content-center" @click="loginRequired()">
              <button class="py-2">채팅하러 가기</button>
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
import { mapGetters , mapActions } from 'vuex'
import router from '@/router'

export default {
  name: 'Leaf82Detail',
  data() {
    return {
      user: {
      },
      addr: {
      },
      info: {
        id: null,
        user: {
          nickname: '',
          photo: '',
          pk: null,
          username: '',
        },
        addr: {
          id: null,
          sido: '',
          sigungu: '',
        },
        plantname: '',
        photo: '',
        created_at: '',
        content: '',
        price: '',
        category_class: '',
        status_class: '',
        posting_addr: null
      },
      deleteInfo: {
        username: this.$route.params.username,
        posting_addr: this.$route.params.posting_addr
      }
    }
  },
  methods: {
    ...mapActions(['deleteLeaf82','setReceiver']),
    fillData() {
      this.user = this.leaf82Detail.user
      this.addr = this.leaf82Detail.addr
      this.info = this.leaf82Detail
      this.info.price = this.info.price.toLocaleString('ko-KR')
    },
    loginRequired() {
      alert('로그인이 필요한 서비스입니다.')
      router.push({ name: 'login' })
    },
    goChat(){
      console.log(this.user.pk)
      this.setReceiver(this.user.username)
    }
  },
  computed: {
    ...mapGetters(['leaf82Detail', 'currentUser', 'isLoggedIn']),
  },
  watch: {
    leaf82Detail() {
      this.fillData()
    }
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
  border-radius: 15px;
}

/* 왼쪽 */
.img-box img{
  height: 300px;
  width: 300px;
  border-radius: 1rem;
}

.update-btn {
  color: white;
  background-color: #b2c9ab;
  border-radius: 5px;
  border: none;
  width: 5rem;
  height: 1.8rem;
}

.update-btn:hover {
  cursor: pointer;
  background-color: #65805d;
  transition: all 0.5s;
}


.delete-btn {
  color: black;
  background-color: white;
  border-color: rgb(170, 170, 170);
  border-style: solid;
  color: gray;
  border-radius: 5px;
  border-width: 1px;
  width: 5rem;
  height: 1.8rem;
}

.delete-btn:hover {
  cursor: pointer;
  background-color: #d2d2d2;
  transition: all 0.5s;
}

/* 오른쪽 */
p {
  margin: 0;
}

.plantname p {
  font-size: 2rem;
  font-weight: bold;
}

.nickname-route {
  text-decoration: none;
  color: black;
}

.user-photo {
  width: 1.5rem;
  height: 1.5rem;
}

.price p {
  font-weight: bold;
}

.status p {
  font-size: 0.8rem;
  color: gray;
}

.addr p {

}

.content p {
  font-size: 0.9rem;
}

.message {
  width: 100%;
}

.message a {
  width: 100%;
  text-decoration: none;
}

.message a button {
  width: 80%;
  background-color: white;
  border-radius: 0.5rem;
  color: gray;
  border-width: 1px;
  border-color: gray;
  border-style: solid;
  font-size: 0.8rem;
}

.message a button:hover {
  cursor: pointer;
  background-color: rgb(206, 206, 206);
  transition: all 0.5s;
}
</style>