<template>
    <div class="search row">
      <div class="col-sm-2 col-md-4 col-0"></div>
      <div class="search-box col-sm-8 col-md-4 col-12 d-flex justify-content-center">
        <input class="search-input" type="text" v-model="info.plantname" placeholder="식물명을 입력해주세요" @keyup.enter="fetchLeaf82(info)">
        <button class="search-btn" type="submit" @click="fetchLeaf82(info)">
          <span class="d-flex align-items-center justify-content-center">검색</span>
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
            <option selected>지역을 선택해주세요</option>
            <option v-for="(loc) in sido" :key="loc.pk" :value="loc.sido">{{ loc.sido }}</option>
          </select>
          <!-- 시도가 선택되면 활성화 -->
          <select class="sigungu" @change="beforeFetchSearch($event)" v-if="this.info.sido">
            <option selected>동네를 선택해주세요</option>
            <option value="" v-for="(loc) in sigungu" :key="loc.pk">{{ loc.sigungu }}</option>
          </select>
          <select class="sigungu" v-if="!this.info.sido" disabled>
            <option selected>동네를 선택해주세요</option>
          </select>
        </div>
      </div>
      <div class="col-sm-2 col-0"></div>
    </div>
</template>

<script>
import { mapActions , mapGetters } from 'vuex'

export default {
  name: 'Leaf82SearchBar',
  data () {
    return {
      info: {
        plantname: '',
        sido: '',
        sigungu: '',
      }
    }
  },
  methods: {
    ...mapActions(['fetchLeaf82', 'fetchSido', 'fetchSigungu', 'search']),
    // 필터링 없이
    beforeSearch() {
      if (this.info.sido === '' || this.info.sigungu === '') {
        const params = {
          plantname : this.info.plantname
        }
        this.search(params)
      } else {
        const params = this.info
        this.search(params)
      }
    },
    // 필터링
    beforeFetchSigungu(event) {
      const sido = event.target.value
      this.info.sido = sido
      this.fetchSigungu(sido)
    },
    beforeFetchSearch(event) {
      const sigungu = event.target.value
      this.info.sigungu = sigungu
      if (this.info.plantname === '') {
        const params = {
          sido: this.info.sido,
          sigungu: this.info.sigungu
        }
        this.search(params)
      } else {
        const params = this.info
        this.search(params)
      }
    }
  },
  computed: {
    ...mapGetters(['sido', 'sigungu', 'isLoggedIn'])
  },
  created() {
    this.fetchLeaf82()
    this.fetchSido()
  },

}
</script>

<style scoped>
div {
  margin: 0;
  padding: 0;
}
.search {
  background-image: url('@/assets/Leaf82/leaf82SearchBarImg.jpg');
  padding-top: 175px;
  padding-bottom: 175px;
}

.search-box {
  position: relative;
}

.search-input {
  width: 80%;
  height: 2.5rem;
  border: 0;
  border-radius: 0.5rem;
  box-shadow: 0rem 0rem 1rem #d2d2d2;
  font-size: 1.2rem;
}

.search-btn {
  width: 20%;
  border: 0;
  background-color: #b2c9ab;
  border-radius: 0.5rem;
  color: white;
  box-shadow: 0rem 0rem 1rem #d2d2d2;
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
  font-size: 0.8rem;
}

.create-btn:hover {
  cursor: pointer;
}

select {
  border-radius: 0.5rem;
  font-size: 0.8rem;
}
</style>