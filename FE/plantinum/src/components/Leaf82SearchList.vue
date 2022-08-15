<template>
  <!-- 서치 배너 -->
  <div class="search row">
    <div class="col-sm-2 col-md-4 col-0"></div>
    <div class="search-box col-sm-8 col-md-4 col-12 d-flex justify-content-center">
      <input class="search-input pl-3" type="text" v-model="info.plantname" placeholder="식물명을 입력해주세요" @keyup.enter="beforeSearch()">        
      <button class="search-btn" type="submit" @click="beforeSearch()">
        <span class="material-symbols-outlined d-flex align-items-center justify-content-center">search</span>
      </button>
    </div>
    <div class="col-sm-2 col-md-4 col-0"></div>
  </div>
  <div class="select-box row mt-5 mb-3">
    <div class="col-sm-2 col-0"></div>
    <div class="select row d-flex justify-content-between col-sm-8 col-12">
      <div class="create">
        <!-- 생성버튼 -->
        <router-link :to="{ name : 'leaf82New' }" v-if="isLoggedIn">
          <button class="create-btn">
            등록
          </button>
        </router-link>
      </div>
      <div class="filter d-flex justify-content-center">
        <!-- 검색버튼 -->
        <select class="sido mr-1" @change="beforeFetchSigungu($event)">
          <option value="null">지역을 선택해주세요</option>
          <option v-for="loc in sido" :key="loc.pk" :value="loc.sido">{{ loc.sido }}</option>
        </select>
        <!-- 시도가 선택되면 활성화 -->
        <select class="sigungu" @change="beforeFetchSearch($event)" v-if="this.info.sido">
          <option selected>동네를 선택해주세요</option>
          <option v-for="loc in sigungu" :key="loc.pk" :value="loc.sigungu">{{ loc.sigungu }}</option>
        </select>
        <select class="sigungu" v-if="!this.info.sido" disabled>
          <option selected>동네를 선택해주세요</option>
        </select>
      </div>
    </div>
    <div class="col-sm-2 col-0"></div>
  </div>
  <!-- 리스트 영역 -->
  <div class="leaf82-sell">
    <!-- 분양해요 활성화 -->
    <div class="title d-flex justify-content-center mb-5" v-if="isSell">
      <span class="sell-on pr-2">분양해요</span>
      <span class="divider"> | </span>
      <span class="buy-off pl-2" @click="onoff()">분양받아요</span>
    </div>
    <!-- 분양해요 목록들 -->
    <div class="leaf82-list-box row pb-2" v-if="isSell">
      <div class="col-sm-2 col-md-3 col-0" v-if="!!sList"></div>
      <!-- 리스트가 있을 때 -->
      <div class="leaf82-list col-sm-8 col-md-6 col-0 row d-flex justify-content-center" v-if="!!sList">
        <div class="item px-3 pb-4" v-for="leaf82 in sList" :key="leaf82.pk">
          <router-link class="route" :to="{ name: 'leaf82Detail', params: { username: leaf82.user.username , posting_addr: leaf82.posting_addr } }">
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
      <div class="col-sm-2 col-md-3 col-0" v-if="!!sList"></div>
      <!-- 리스트가 없을때 -->
      <div class="col-sm-2 col-md-3 col-0" v-if="!sList[0]"></div>
      <div class="leaf82-list col-sm-8 col-md-6 col-0 mt-5" v-if="!sList[0]">
        <div class="d-flex justify-content-center">
          <span class="material-symbols-outlined noplant-icon">macro_off</span>
        </div>
        <div class="noplant-text d-flex justify-content-center">
          <p>등록된 식물이 없습니다.</p>
        </div>
      </div>
      <div class="col-sm-2 col-md-3 col-0" v-if="!sList[0]"></div>
    </div>
    <!-- 분양받아요 활성화 -->
    <div class="title d-flex justify-content-center mb-5" v-if="!isSell">
      <span class="sell-off pr-2" @click="onoff()">분양해요</span>
      <span class="divider"> | </span>
      <span class="buy-on pl-2">분양받아요</span>
    </div>
    <!-- 분양받아요 목록들 -->
    <div class="leaf82-list-box row pb-2" v-if="!isSell">
      <div class="col-sm-2 col-md-3 col-0" v-if="!!bList"></div>
      <!-- 리스트가 있을 때 -->
      <div class="leaf82-list col-sm-8 col-md-6 col-0 row d-flex justify-content-center" v-if="!!bList">
        <div class="item px-2 pb-2" v-for="leaf82 in bList" :key="leaf82.pk">
          <router-link class="route" :to="{ name: 'leaf82Detail', params: { username: leaf82.user.username , posting_addr: leaf82.posting_addr } }">
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
      <div class="col-sm-2 col-md-3 col-0" v-if="!!bList"></div>
      <!-- 리스트가 없을때 -->
      <div class="col-sm-2 col-md-3 col-0" v-if="!bList[0]"></div>
      <div class="leaf82-list col-sm-8 col-md-6 col-0 mt-5" v-if="!bList[0]">
        <div class="d-flex justify-content-center">
          <span class="material-symbols-outlined noplant-icon">macro_off</span>
        </div>
        <div class="noplant-text d-flex justify-content-center">
          <p>등록된 식물이 없습니다.</p>
        </div>
      </div>
      <div class="col-sm-2 col-md-3 col-0" v-if="bList[0]"></div>
    </div>
    <!-- 더보기 버튼 -->
    <div class="d-flex justify-content-center pb-5" v-if="isSell">
      <button class="more-btn" v-if="!!sellObject.next" @click="more()">- 더보기 -</button>
    </div>
    <div class="d-flex justify-content-center pb-5" v-if="!isSell">
      <button class="more-btn" v-if="!!buyObject.next" @click="more()">- 더보기 -</button>
    </div>
  </div>
</template>

<script>
import { mapActions , mapGetters } from 'vuex'

export default {
  name: 'Leaf82SearchList',
  data () {
    return {
      isSell: true,
      info: {
        plantname: '',
        sido: '',
        sigungu: '',
        limit: 20,
        page: 1,
        category_class: '분양해요',
      },
      bList: [],
      sList: []
    }
  },
  methods: {
    ...mapActions(['fetchSigungu', 'search',]),
    // 초기화
    fetchSearch() {
      const params = {
        limit : this.info.limit,
        page: this.info.page,
        category_class: '분양해요',
      }
      this.search(params)
    },
    // 필터링 없이
    beforeSearch() {
      if (!!this.info.plantname === true && !!this.info.sido === true && !!this.info.sigungu === true) {
        this.info.page = 1
        const params = this.info
        this.search(params)
      } else if (!!this.info.plantname === true && !!this.info.sigungu === false) {
        this.info.page = 1
        const params = {
          plantname : this.info.plantname,
          limit: this.info.limit,
          page: this.info.page,
          category_class: this.info.category_class,
        }
        this.search(params)
      } else if (!!this.info.plantname === false && !!this.info.sido === true && !!this.info.sigungu === true) {
        this.info.page = 1
        const params = {
          sido: this.info.sido,
          sigungu: this.info.sigungu,
          limit: this.info.limit,
          page: this.info.page,
          category_class: this.info.category_class,
        }
        this.search(params)
      } else if (!!this.info.plantname === false && !!this.info.sido === false && !!this.info.sigungu === false) {
        const params = {
          limit: this.info.limit,
          page: this.info.page,
          category_class: this.info.category_class,
        }
        this.search(params)
      }
    },
    // 필터링
    beforeFetchSigungu(event) {
      const sido = event.target.value
      if (sido === 'null') {
        if (this.info.plantname !== '') {
          this.info.sido = ''
          this.info.sigungu = ''
          this.info.page = 1
          if (this.isSell) {
            const params = {
              plantname: this.info.plantname,
              page: this.info.page,
              limit: this.info.limit,
              category_class: '분양해요'
            }
            this.search(params)
          } else {
            const params = {
              plantname: this.info.plantname,
              page: this.info.page,
              limit: this.info.limit,
              category_class: '분양받아요'
            }
            this.search(params)
          }
        } else {
          this.info.sido = ''
          this.info.sigungu = ''
          this.info.page = 1
          if (this.isSell) {
            const params = {
            category_class: '분양해요',
            page: this.info.page,
            limit: this.info.limit
            }
            this.search(params)
          } else {
            const params = {
            category_class: '분양받아요',
            page: this.info.page,
            limit: this.info.limit
            }
            this.search(params)
          }
        }       
      } else {
        this.info.sido = sido
        this.fetchSigungu(sido)
      }
    },
    beforeFetchSearch(event) {
      const sigungu = event.target.value
      this.info.sigungu = sigungu
      if (this.info.plantname === '') {
        this.info.page = 1
        const params = {
          sido: this.info.sido,
          sigungu: this.info.sigungu,
          category_class: this.info.category_class,
          page: this.info.page,
          limit: this.info.limit
        }
        this.search(params)
      } else {
        this.info.page = 1
        const params = this.info
        this.search(params)
      }
    },
    onoff() {
      this.isSell = !this.isSell
      if(this.isSell) {
        this.info.category_class = '분양해요'
      } else {
        this.info.category_class = '분양받아요'
      }
      if (this.isSell) {
        if (!!this.info.plantname && !!this.info.sigungu) {
          this.info.page = 1
          this.search(this.info)
        } else if (!!this.info.plantname && !this.info.sigungu) {
          this.info.page = 1
          const params ={
            plantname: this.info.plantname,
            category_class: this.info.category_class,
            page: this.info.page,
            limit: this.info.limit
          }
          this.search(params)          
        } else if (!this.info.plantname && !!this.info.sigungu) {
          this.info.page = 1
          const params ={
            sido: this.info.sido,
            sigungu: this.info.sigungu,
            category_class: this.info.category_class,
            page: this.info.page,
            limit: this.info.limit
          }
          this.search(params)          
        } else {
          this.info.page = 1
          const params ={
            category_class: this.info.category_class,
            page: this.info.page,
            limit: this.info.limit
          }
          this.search(params)            
        }
      } else {
        if (!!this.info.plantname && !!this.info.sigungu) {
          this.info.page = 1
          this.search(this.info)
        } else if (!!this.info.plantname && !this.info.sigungu) {
          this.info.page = 1
          const params ={
            plantname: this.info.plantname,
            category_class: this.info.category_class,
            page: this.info.page,
            limit: this.info.limit
          }
          this.search(params)          
        } else if (!this.info.plantname && !!this.info.sigungu) {
          this.info.page = 1
          const params ={
            sido: this.info.sido,
            sigungu: this.info.sigungu,
            category_class: this.info.category_class,
            page: this.info.page,
            limit: this.info.limit
          }
          this.search(params)          
        } else {
          this.info.page = 1
          const params ={
            category_class: this.info.category_class,
            page: this.info.page,
            limit: this.info.limit
          }
          this.search(params)
        }
      }
    },
    fillList() {
      this.sList = this.sellList
      this.bList = this.buyList
      for (let item of this.sList) {
        const price = Number(item.price)
        item.price = price.toLocaleString('ko-KR')
        if (item.plantname.length > 7) {
          const plantname = item.plantname.substr(0, 7) + '...'
          item.plantname = plantname
        }
      }
      for (let item of this.bList) {
        const price = Number(item.price)
        item.price = price.toLocaleString('ko-KR')
        if (item.plantname.length > 7) {
          const plantname = item.plantname.substr(0, 7) + '...'
          item.plantname = plantname
        }
      }
    },
    more() {
      this.info.page += 1
      const params = this.info
      if (!this.info.plantname) {
        delete params.plantname
      }
      if (!this.info.sigungu) {
        delete params.sigungu,
        delete params.sido
      }
      this.search(params)
    }
  },
  computed: {
    ...mapGetters(['sido', 'sigungu', 'isLoggedIn', 'sellObject', 'sellList', 'buyObject', 'buyList'])
  },
  created() {
    this.fetchSearch()
  },
  watch: {
    sellList() {
      this.fillList()
    },
    buyList() {
      this.fillList()
    }
  }
}
</script>

<style scoped>
div {
  margin: 0;
  padding: 0;
}
.search {
  background: url('@/assets/Leaf82/searchbar_pic_0.jpg') bottom right;
  padding-top: 175px;
  padding-bottom: 175px;
  background-size: cover;
}

.search-box {
  position: relative;
  border-radius: 0.5rem;
  box-shadow: 0rem 0rem 1rem #d2d2d2;

}

.search-input {
  width: 90%;
  height: 2.5rem;
  border: 0;
  border-top-left-radius: 0.5rem;
  border-bottom-left-radius: 0.5rem;
  font-size: 1.2rem;
}

.search-input:focus {
  outline: none;
}

.search-btn {
  width: 10%;
  border: 0;
  background-color: white;
  border-top-right-radius: 0.5rem;
  border-bottom-right-radius: 0.5rem;
  color: black;
}

.search-btn:focus {
  outline: none;
}

.search-btn:hover {
  cursor: pointer;
}

.create {
  width: 4rem;
}

.create-btn {
  width: 100%;
  border: none;
  background-color: #b2c9ab;
  color: white;
  border-radius: 0.5rem;
  font-size: 0.9rem;
  height: 1.8rem;
}

.create-btn:focus {
  outline: none;
}

.create-btn:hover {
  cursor: pointer;
  background-color: #65805d;
  transition: all 0.5s;
}


select {
  border-radius: 0.5rem;
  font-size: 0.9rem;
  border-color: rgb(191, 191, 191); 
  height: 1.8rem; 
}

select:focus {
  outline: none;
}

/* 리스트 영역 */

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

.more-btn {
  background-color: transparent;
  border: none;
  color: #7E7E7E;
}

.more-btn:hover {
  cursor: pointer;
  color: #65805d;
}
</style>