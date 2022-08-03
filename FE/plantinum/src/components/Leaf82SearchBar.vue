<template>
  <div>
    <div class="search row">
      <div class="col-sm-2 col-md-4 col-0"></div>
      <!-- <input class="search-input" type="text" v-model="info.keyword" placeholder="식물명을 입력해주세요" @keyup.enter="fetchLeaf82(info)">
      <button class="search-btn" type="submit" @click="fetchLeaf82(info)"></button> -->
      <div class="search-box col-sm-8 col-md-4 col-12 d-flex justify-content-center">
        <input class="search-input" type="text" v-model="info.keyword" placeholder="식물명을 입력해주세요">
        <button class="search-btn" type="submit">
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
          <button class="create-btn">
            등록
          </button>
        </div>
        <div class="filter d-flex justify-content-center">
          <!-- 검색버튼 -->
          <!-- <select name="sido" id="">
            <option :v-for="(s) in sido" @click="updateAndfetchSigungu(s)">{{ s }}</option>
          </select> -->
          <select name="sido" id="">
            <option>서울시</option>
            <option>서울시</option>
          </select>
          <select name="sido" id="">
            <option>동대문구</option>
            <option>서대문구</option>
          </select>
        </div>
      </div>
      <div class="col-sm-2 col-0"></div>
    </div>
  </div>
</template>

<script>
import { mapActions , mapGetters } from 'vuex'

export default {
  name: 'Leaf82SearchBar',
  data () {
    return {
      info: {
        keyword: '',
        sido: '',
        sigungu: '',
      }
    }
  },
  methods: {
    ...mapActions(['fetchLeaf82', 'fetchSido', 'fetchSigungu', 'searchAll']),
    updateAndfetchSigungu(sido) {
      this.info.sido = sido
      this.fetchSigungu(sido)
    },
    searchFilter(sigungu) {
      this.info.sigungu = sigungu
      this.searchAll(this.info)
    }
  },
  computed: {
    ...mapGetters(['sido'])
  },
  created() {
    this.fetchSido()
  }

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
}

</style>